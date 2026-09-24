# Primary References

Use primary standards and official guidance. Prefer stable, versioned references for release claims.

## Accessibility
- W3C WCAG 2.2: https://www.w3.org/TR/WCAG22/
- W3C What's New in WCAG 2.2: https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/
- WAI-ARIA: https://www.w3.org/WAI/standards-guidelines/aria/
- ARIA Authoring Practices Guide: https://www.w3.org/WAI/ARIA/apg/
- ARIA patterns: https://www.w3.org/WAI/ARIA/apg/patterns/
- ARIA practices: https://www.w3.org/WAI/ARIA/apg/practices/

## Cybersecurity
- OWASP Top 10:2025: https://top10.owasp.org/2025/
- OWASP ASVS 5.0.0: https://owasp.org/projects/asvs
- OWASP WSTG project: https://owasp.org/projects/web-security-testing-guide
- OWASP WSTG v4.2 stable: https://wstg.owasp.org/v4.2/
- OWASP Cheat Sheet Series: https://cheatsheetseries.owasp.org/
- OWASP XSS Prevention Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html
- OWASP Authentication Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html

## Secure development
- NIST SP 800-218, Secure Software Development Framework (SSDF) 1.1: https://csrc.nist.gov/pubs/sp/800/218/final
- NIST SSDF project: https://csrc.nist.gov/projects/ssdf

## Privacy
- NIST Privacy Framework: https://www.nist.gov/privacy-framework
- Stable Privacy Framework 1.0: https://www.nist.gov/privacy-framework/privacy-framework

Note: newer Privacy Framework drafts may exist. Treat draft material as draft and do not present it as a final standard.

## Performance
- web.dev Core Web Vitals: https://web.dev/articles/vitals
- Chrome/web.dev performance guidance may be used for implementation details, but actual performance claims require runtime measurement.

## Agent skill format
- OpenAI skills guidance: https://developers.openai.com/plugins/concepts/skills
- OpenAI build skills: https://developers.openai.com/plugins/build/skills
- OpenAI Academy — Using skills: https://openai.com/academy/skills/

## Review principles
- Prefer native HTML semantics before ARIA.
- Treat ARIA Authoring Practices examples as patterns to understand and test, not production code to copy blindly.
- Treat OWASP Top 10 as an awareness/risk baseline, not a complete verification standard; use ASVS/WSTG/Cheat Sheets for deeper verification.
- Do not claim security, accessibility, privacy, or performance compliance from static frontend inspection alone.
- Separate stable standards from development/latest drafts.
