---
layout: default
title: "Google Maps leads into your CRM: a setup checklist for 5 paths"
description: "How to connect HubSpot, Zoho CRM, Pipedrive, Freshsales or a webhook so Google Maps leads land in your CRM without a spreadsheet step."
---

# Google Maps leads into your CRM: a setup checklist for 5 paths

*By Tarun Kumar · 15 November 2026*

Most Google Maps leads stall out in a spreadsheet — exported, cleaned, imported, half forgotten. Mantis removes that middle step: it connects to HubSpot, Zoho CRM, Pipedrive, Freshsales, or any webhook (Zapier, Make, n8n), so leads go straight from Google Maps into your CRM.

## One setup, three moves

Every path is the same three moves:

1. In your CRM, create or copy the credential: a token, an API key, a grant code, or a webhook URL.
2. In Mantis, paste it and connect — Mantis verifies the credential with the CRM before saving, stores it encrypted, and never shows it again.
3. Select your Google Maps leads and click **Send to CRM** — up to 500 at a time, and re-sending updates the same record.

## The 5 paths at a glance

| Path | What you paste | What each lead becomes | Re-send matching |
| --- | --- | --- | --- |
| **HubSpot** | Private app access token (pat-…), 4 scopes: companies read/write, contacts read/write | Company + Contact when there is a person or email | Company by domain, then name |
| **Zoho CRM** | Client ID, Client secret, grant code from a Self Client | Zoho Lead (Company, Last name, Email, Phone, Website, City, Lead source "Mantis") | Same record updated |
| **Pipedrive** | Company domain (before .pipedrive.com) + personal API token | Organization + linked Person when the lead has a person, email, or phone | Organization by exact name |
| **Freshsales** | Bundle alias (acme.myfreshworks.com) + API key | Account + linked Contact when there is an email or phone | Account upserted on name |
| **Webhook** | An https URL from Zapier, Make, n8n, or any endpoint accepting a JSON POST | One JSON POST per lead | First send lead.created; re-send lead.updated |

## Notes on each path

**HubSpot.** Create a private app token with the four scopes above. HubSpot changed how new tokens are created in October 2026; the [HubSpot guide](https://mantisai.in/resources/send-google-maps-leads-to-hubspot?utm_source=github-pages&utm_medium=guest&utm_campaign=gp) covers the current steps.

**Zoho CRM.** In Zoho's API console for your domain (api-console.zoho.in, .com, .eu or .com.au), add a **Self Client** and generate a code with scope ZohoCRM.modules.leads.ALL,ZohoCRM.org.READ and a 10-minute duration. Pick the matching data centre in Mantis, then paste the Client ID, Client secret, and code. The code works once and only inside its window, so connect immediately — Mantis swaps it for a lasting token straight away. Zoho's [OAuth overview](https://www.zoho.com/crm/developer/docs/api/v8/oauth-overview.html) explains Self Clients in more detail.

**Pipedrive.** Find your token under **Settings → Personal preferences → API**; Pipedrive documents this in [how to find the API token](https://pipedrive.readme.io/docs/how-to-find-the-api-token). Paste it into Mantis together with your company domain.

**Freshsales.** Under **Settings → API Settings**, copy your bundle alias (acme.myfreshworks.com; older accounts use acme.freshsales.io) and your API key. One catch: Freshsales will not save a contact that has neither an email nor a phone number.

**Webhook.** Use this path when your CRM is not one of the four. Get a URL — Zapier: **Webhooks by Zapier → Catch Hook**; Make: **Webhooks → Custom webhook**; n8n: a **Webhook** node set to POST, using the **Production URL**. Mantis sends one signed ping and needs a 2xx back; only public https URLs are accepted, and redirects are not followed. Each lead then goes out as one JSON POST — lead.created first, lead.updated on re-send.

If you set a signing secret, every request carries two headers, X-Mantis-Timestamp and X-Mantis-Signature; the signature is a sha256 HMAC of the timestamp, a dot, and the raw request body. Recompute it with the same secret, compare, and reject requests whose timestamps are old.

## Which path fits

None of the five is better than the others — pick the CRM your team already works in:

- Companies plus contacts → **HubSpot**
- Zoho's Leads module before converting → **Zoho CRM**
- A deal pipeline built around organizations → **Pipedrive**
- Freshworks accounts with linked contacts → **Freshsales**
- Any other CRM, or heavier automation per lead → **webhook**

Still comparing ways to pull leads from Google Maps itself? Compare scrapers on cost, fields and limits before you pick a CRM path.

## FAQ

**Will re-sending create duplicates?**
No — re-sending updates the same record. HubSpot matches by domain, then name; Pipedrive matches the organization by exact name; Freshsales upserts the account on name; webhook receivers get a lead.updated event instead of a second lead.created.

**What happens if I disconnect?**
Leads you already sent stay in the CRM. The saved credential was stored encrypted and never shown again after you pasted it.

---

I'm Tarun, founder of Mantis. To try the integrations, [Mantis](https://mantisai.in?utm_source=github-pages&utm_medium=guest&utm_campaign=gp) gives 500 free credits once at signup, no card.
