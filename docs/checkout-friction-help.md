# Checkout friction help without private details

Marker: `CHECKOUT_FRICTION_HELP_2026_07_07` `PAYMENT_FRICTION_PUBLIC_SAFE_HELP_2026_07_07_2316`

Use this page if the Payhip page, payment step, download step, or pre-purchase decision gets confusing and you want help without exposing private repository or billing details.

## Fast path

1. Run the free scanner first so the buy/skip question is concrete.
2. Re-open the product page from the public link: <https://payhip.com/b/1nmxV>.
3. If the page is unavailable, confusing, a payment option will not complete, or the page does not match the public description, open the public-safe buyer support form: <https://github.com/el-zachariah/ai-agent-safety-starter-pack/issues/new?template=buyer-question.yml>.
4. If you already downloaded the ZIP and something does not match, run the local verifier first, then use the same support form with only public-safe details.

## If the payment step does not complete

Use the buyer support form instead of posting screenshots or account details. Include only public-safe facts:

- free scan result: Green / Yellow / Red / not run yet,
- where it stalled: Payhip product page / checkout frame / PayPal option / card option / after clicking buy,
- non-secret symptom text such as `button looped`, `generic checkout error`, or `payment option unavailable`,
- what answer would let you decide whether to try checkout again.

Do not include names, email addresses, card digits, billing addresses, payment-provider screenshots, account dashboards, order identifiers, or private repository details. `PAYMENT_FRICTION_PUBLIC_SAFE_HELP_2026_07_07_2316`

## What to include in a public issue

Copy this shape and remove anything that is not public-safe:

```text
Context: I ran the free scanner and my result was Green / Yellow / Red.
Where I got stuck: product page / checkout wording / payment step / download / ZIP verifier / install step.
Public-safe symptom: <short non-secret error text or confusing step>.
What would help: <what answer would let me decide or continue>.
```

## What not to include

Do not paste private code, secrets, credentials, customer data, card details, billing data, payment-provider screenshots, order identifiers, private repo URLs, or account dashboards into public GitHub issues.

## Buy / skip reminder

Buy the `$7` pack only when the free scan is Yellow/Red or when you need a reusable handoff workflow, destructive-command hook example, report template, demo risky repo, and verifier for repeated AI-agent runs. If the scan is Green, keep using the free lite scanner and normal review.
