# studiotopeira.com

The studio's site: a landing page (English at `/`, Portuguese at `/pt/`, Spanish at `/es/`) and Iara's privacy and support pages
(`/iara/privacy/`, `/iara/support/`). Plain static files; no build step is needed to host it.

- Change a text: edit `build.py` (the texts are at the top), run `python3 build.py`, commit the result.
- When Iara is on a store: put its address in `STORE_IOS` (App Store) or `STORE_ANDROID` (Google Play) in `build.py`
  and rebuild; that store's button becomes a link, and the other still says "coming soon" until it has an address too.
- Preview: `python3 -m http.server 8765` in this folder, then open http://localhost:8765.
- The font (Amatic SC, SIL Open Font License) and the images are served from `assets/`; nothing loads from another site.

Live at https://studiotopeira.com since 2026-10-03, served by GitHub Pages from this repository's `main` branch (the
repository is public for that reason). A push to `main` publishes within a minute. DNS is at Cloudflare (the account
that came with the iCloud purchase): CNAME `@` and `www` to `gusfelhberg.github.io`, both "DNS only"; the MX, TXT and
`sig1._domainkey` records there are iCloud Mail's and must stay.
