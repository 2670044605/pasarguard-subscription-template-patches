# 0001 english default and minimal debranding

## Goal
Keep the official PasarGuard subscription template behavior, while making the default production artifact English-first and removing footer-level promotional/support elements.

## Patch scope
- `src/i18n/config.ts`
  - change default fallback language from `fa` to `en`
- `.github/workflows/release.yml`
  - change default packaged artifact from Persian to English
- `src/components/layout/footer.tsx`
  - remove support URL entry
  - remove footer credit line

## Why this patch exists
- The user wants the subscription template to be maintained as a long-term, reviewable patch set.
- English should be the default published/deployed variant.
- Footer-level branding/support prompts are outside the desired minimal UI scope.

## Risk profile
- Low risk: frontend-only patch, no backend/API/database changes.
- Does not modify PasarGuard core behavior.
- Only affects subscription page presentation and build defaults.
