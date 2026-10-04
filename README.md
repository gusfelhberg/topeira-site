# studiotopeira.com

The studio's site: a landing page (English at `/`, Portuguese at `/pt/`) and Iara's privacy and support pages
(`/iara/privacy/`, `/iara/support/`). Plain static files; no build step is needed to host it.

- Change a text: edit `build.py` (the texts are at the top), run `python3 build.py`, commit the result.
- When Iara is on the App Store: put its address in `STORE` in `build.py` and rebuild; the button becomes a link.
- Preview: `python3 -m http.server 8765` in this folder, then open http://localhost:8765.
- The font (Amatic SC, SIL Open Font License) and the images are served from `assets/`; nothing loads from another site.

Not published yet (2026-10-03): hosting and the domain's DNS are the owner's steps. See `studio/apps/iara/README.md`
and `company/DECISIONS.md` in the `hq` repository.
