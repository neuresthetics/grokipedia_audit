# Concept C2: centered, enlarged, procedurally redrawn lens. Only the white Grok mark comes from source.
import importlib.util,sys
from PIL import Image, ImageDraw, ImageFilter, ImageFont
import numpy as np, random
SRC='/workspace/neuresthetics.github.io/assets/img/cards/card-grokipedia.jpg'
a=np.array(Image.open(SRC).convert('RGB')).astype(float)
CX,CY,RIN,ROUT=384.5,191.5,138,158
F='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'; FB='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
GOLD=(212,167,44); GRN=(76,201,110); RED=(232,84,84); AMB=(240,170,50); BG=(9,10,14)
def font(p,s): return ImageFont.truetype(p,max(6,int(s)))
# --- logo mask: crop around logo, soft luminance mask, upscale then re-sharpen edge with smoothstep
lum=a.mean(2); yy,xx=np.mgrid[:450,:900]
lm=np.clip((lum-90)/120,0,1)*(((xx-CX)**2+(yy-CY)**2)<(RIN-8)**2)
c0=int(CX-RIN); r0=int(CY-RIN); crop=lm[r0:r0+2*RIN, c0:c0+2*RIN]  # square centered-ish
LOGO_OFF=(CX-c0, CY-r0)
def logo_mask(scale):
    m=Image.fromarray((crop*255).astype('uint8')).filter(ImageFilter.GaussianBlur(0.6))
    n=int(crop.shape[0]*scale); m=np.array(m.resize((n,n),Image.BICUBIC)).astype(float)/255
    t=np.clip((m-0.35)/0.3,0,1); t=t*t*(3-2*t)  # crisp antialiased edge
    return Image.fromarray((t*255).astype('uint8'))
def mark(d,x,y,r,kind):
    c={'ok':GRN,'x':RED,'a':AMB}[kind]; d.ellipse([x-r,y-r,x+r,y+r],fill=c+(240,)); w=max(2,int(r*.32))
    if kind=='ok': d.line([(x-r*.45,y),(x-r*.1,y+r*.38),(x+r*.5,y-r*.4)],fill=(10,20,12),width=w,joint='curve')
    elif kind=='x':
        d.line([(x-r*.4,y-r*.4),(x+r*.4,y+r*.4)],fill=(25,8,8),width=w); d.line([(x-r*.4,y+r*.4),(x+r*.4,y-r*.4)],fill=(25,8,8),width=w)
    else: d.line([(x,y-r*.5),(x,y+r*.15)],fill=(30,20,5),width=w); d.ellipse([x-w*.6,y+r*.35-w*.6,x+w*.6,y+r*.35+w*.6],fill=(30,20,5))
def glow(img,cx,cy,r,col,amt):
    g=Image.new('RGBA',img.size,(0,0,0,0)); ImageDraw.Draw(g).ellipse([cx-r,cy-r,cx+r,cy+r],fill=col+(amt,))
    img.alpha_composite(g.filter(ImageFilter.GaussianBlur(r*.45)))
def radial(W,H,cx,cy,r,inner,outer,ox=0,oy=0):
    yy,xx=np.mgrid[:H,:W]; t=np.clip(np.sqrt((xx-cx-ox)**2+(yy-cy-oy)**2)/r,0,1)[...,None]
    return np.array(inner)*(1-t)+np.array(outer)*t
def disc_alpha(W,H,cx,cy,r,aa=1.5):
    yy,xx=np.mgrid[:H,:W]; return np.clip((r-np.sqrt((xx-cx)**2+(yy-cy)**2))/aa+.5,0,1)
def layer(rgb,alpha):
    return Image.fromarray(np.dstack([np.clip(rgb,0,255),alpha*255]).astype('uint8'),'RGBA')
def render(W,H,u,wide,seed=7):
    rng=random.Random(seed)
    R=H*(0.455 if not wide else 0.465); cx,cy=W/2,H/2; rin=R*RIN/ROUT
    img=Image.new('RGBA',(W,H),BG+(255,)); d=ImageDraw.Draw(img); step=int(24*u)
    for x in range(step//2,W,step):
        for y in range(step//2,H,step): d.ellipse([x-u*.8,y-u*.8,x+u*.8,y+u*.8],fill=(40,44,52,255))
    # verdict ledger (real Spinoza as-linked proportions)
    L=Image.new('RGBA',(W,H),(0,0,0,0)); dl=ImageDraw.Draw(L); cell=int(10*u)
    cols=[GRN]*30+[(200,200,120)]*81+[RED]*73+[(200,90,160)]*94+[(110,110,130)]*47+[(70,70,80)]*76; rng.shuffle(cols); k=0
    for y in range(int(H*0.08),int(H*0.92)-cell,cell+int(4*u)):
        for x in range(int(W*0.04),W-int(W*0.04)-cell,cell+int(4*u)):
            dl.rounded_rectangle([x,y,x+cell,y+cell],radius=int(2*u),fill=cols[k%len(cols)]+(80,)); k+=1
    img.alpha_composite(L.filter(ImageFilter.GaussianBlur(2.5*u)))
    rays=Image.new('RGBA',(W,H),(0,0,0,0)); dr=ImageDraw.Draw(rays)
    for t in np.linspace(0,2*np.pi,48,endpoint=False):
        dr.line([(cx+R*np.cos(t),cy+R*np.sin(t)),(cx+W*np.cos(t),cy+W*np.sin(t))],fill=GOLD+(28,),width=int(u))
    img.alpha_composite(rays.filter(ImageFilter.GaussianBlur(1.5*u)))
    glow(img,cx,cy,R*1.35,GOLD,80)
    yy,xx=np.mgrid[:H,:W]; v=np.clip(1-.75*(((xx-W/2)/(W/1.6))**2+((yy-H/2)/(H/1.3))**2),0.15,1)
    arr=np.array(img).astype(float); arr[...,:3]*=v[...,None]; img=Image.fromarray(arr.astype('uint8'))
    # handle (45° down-right, runs off frame)
    ang=np.deg2rad(42); dx,dy=np.cos(ang),np.sin(ang); px,py=-dy,dx
    def seg(r0,r1,w):
        p0=(cx+dx*r0,cy+dy*r0); p1=(cx+dx*r1,cy+dy*r1)
        return [(p0[0]+px*w,p0[1]+py*w),(p1[0]+px*w,p1[1]+py*w),(p1[0]-px*w,p1[1]-py*w),(p0[0]-px*w,p0[1]-py*w)]
    hw=R*0.085; H_=Image.new('RGBA',(W,H),(0,0,0,0)); dh=ImageDraw.Draw(H_)
    dh.polygon(seg(R*0.95,R*1.12,hw*0.7),fill=(45,47,54,255))            # neck
    dh.polygon(seg(R*1.10,R*1.24,hw*1.05),fill=GOLD+(255,))              # ferrule
    dh.polygon(seg(R*1.13,R*1.16,hw*1.06),fill=(150,115,25,255))
    dh.polygon(seg(R*1.24,R*4,hw*1.2),fill=(26,27,32,255))               # grip
    dh.polygon(seg(R*1.24,R*4,hw*0.25),fill=(70,72,82,140))              # sheen
    sh=Image.new('RGBA',(W,H),(0,0,0,0)); sh.paste((0,0,0,170),(int(10*u),int(14*u)),H_.getchannel('A'))
    sd=Image.new('RGBA',(W,H),(0,0,0,0)); ImageDraw.Draw(sd).ellipse([cx-R+10*u,cy-R+14*u,cx+R+10*u,cy+R+14*u],fill=(0,0,0,190))
    sh.alpha_composite(sd); img.alpha_composite(sh.filter(ImageFilter.GaussianBlur(14*u)))
    img.alpha_composite(H_.filter(ImageFilter.GaussianBlur(0.5*u)))
    # rim: metallic dark grey ring with light top-left
    rim=radial(W,H,cx,cy,R*1.4,(95,98,108),(28,29,34),-R*.4,-R*.4)
    ring=disc_alpha(W,H,cx,cy,R)
    img.alpha_composite(layer(rim,ring))
    # gold ring
    img.alpha_composite(layer(np.full((H,W,3),GOLD,float),disc_alpha(W,H,cx,cy,rin+3.2*u)))
    # glass
    glass=radial(W,H,cx,cy,rin*1.25,(34,35,40),(8,8,11),-rin*.25,-rin*.3)
    img.alpha_composite(layer(glass,disc_alpha(W,H,cx,cy,rin)))
    # in-lens dot grid (sharper, magnified)
    G=Image.new('RGBA',(W,H),(0,0,0,0)); dg=ImageDraw.Draw(G); st=int(36*u*R/(0.455*450*u)*0.6)
    for x in np.arange(cx%st,W,st):
        for y in np.arange(cy%st,H,st): dg.ellipse([x-1.3*u,y-1.3*u,x+1.3*u,y+1.3*u],fill=(70,74,84,200))
    # markers rows
    f=font(FB,13*u*rin/(140*u if wide else 175*u)*1.15); kinds=['ok','x','a','ok']
    for i,kf in enumerate([-0.78,-0.60,0.60,0.78]):
        y=cy+kf*rin; half=np.sqrt(max(rin**2-(y-cy)**2,0))*0.90; x0,x1=cx-half,cx+half
        dg.rounded_rectangle([x0,y-3*u,x0+(x1-x0)*0.52,y+3*u],radius=3*u,fill=(225,228,235,120))
        t=f'[{89+i}]'; tx=x0+(x1-x0)*0.56; bb=f.getbbox(t)
        dg.text((tx,y-(bb[1]+bb[3])/2),t,font=f,fill=GOLD+(255,))
        rr=f.size*0.48; mark(dg,tx+f.getlength(t)+rr*1.6,y,rr,kinds[i])
    G.putalpha(Image.fromarray((np.array(G.getchannel('A'))*disc_alpha(W,H,cx,cy,rin-2*u)).astype('uint8')))
    img.alpha_composite(G)
    # Grok mark
    sc=rin/RIN; m=logo_mask(sc); lo=Image.new('RGBA',m.size,(246,246,248,0)); lo.putalpha(m)
    img.alpha_composite(lo,(int(round(cx-LOGO_OFF[0]*sc)),int(round(cy-LOGO_OFF[1]*sc))))
    # inner glow + highlight
    gr=Image.new('RGBA',(W,H),(0,0,0,0)); ImageDraw.Draw(gr).ellipse([cx-rin,cy-rin,cx+rin,cy+rin],outline=GOLD+(120,),width=int(5*u))
    img.alpha_composite(gr.filter(ImageFilter.GaussianBlur(4*u)))
    hl=Image.new('RGBA',(W,H),(0,0,0,0)); dh=ImageDraw.Draw(hl)
    dh.arc([cx-rin*.88,cy-rin*.88,cx+rin*.88,cy+rin*.88],200,250,fill=(255,255,255,70),width=int(rin*.06))
    dh.ellipse([cx-rin*.62-rin*.04,cy-rin*.55-rin*.04,cx-rin*.62+rin*.04,cy-rin*.55+rin*.04],fill=(255,255,255,120))
    img.alpha_composite(hl.filter(ImageFilter.GaussianBlur(rin*.025)))
    if not wide:  # label on left, clear of the lens
        d=ImageDraw.Draw(img); f1=font(FB,28*u); f2=font(F,12*u); tx=W*0.035; ty=H*0.08
        d.text((tx,ty),'Grokipedia',font=f1,fill=(240,240,244)); d.text((tx,ty+36*u),'AUDIT  ·  claim → source',font=f2,fill=GOLD)
    return img.convert('RGB')
for nm,(w,h,wide) in {'wide':(900,300,True),'card':(900,450,False)}.items():
    big=render(w*2,h*2,2,wide); big.save(f'C2_{nm}@2x.png')
    big.resize((w,h),Image.LANCZOS).save(f'C2_{nm}.jpg',quality=92)
S=Image.new('RGB',(1880,680),(22,23,28)); d=ImageDraw.Draw(S)
d.text((40,20),'Concept C2 — wide 900x300 · card 900x450 · wide @400px',font=font(FB,26),fill=GOLD)
S.paste(Image.open('C2_wide.jpg'),(40,80)); S.paste(Image.open('C2_card.jpg'),(960,80))
S.paste(Image.open('C2_wide.jpg').resize((400,133),Image.LANCZOS),(40,420))
S.paste(Image.open('C2_card.jpg').resize((400,200),Image.LANCZOS),(480,420))
d.text((40,640),'400px previews',font=font(F,16),fill=(150,150,160))
S.save('options_C2.png')
