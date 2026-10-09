# Check prompt: do these non-medical survivors rest on the HIV/STI or cancer claims?

Scope: the surviving male pro arguments tagged E (ethics, rights or law), R (religion, culture or tradition) or O (other) in `../../topic_tags/`, whose own text names HIV, an STI or cancer (keyword list in `../scripts/build_whatif_total.py`). These were never put through the HIV/STI or cancer what-if passes.

For each sentence, with the sentence before it as context, answer:

- **Y**: the sentence's point rests on the HIV/STI protection claim or the cancer-prevention claim. If removing that claim leaves another point (consent, culture, another medical benefit), answer N.
- **N**: the point does not rest on either claim, or another point remains without it, or the sentence only reports a view or an event.

Give a one-line reason for every answer. This is a what-if check: Y means "depends on the claim", not that the claim is wrong. Recorded as a model's judgment, not a person's.
