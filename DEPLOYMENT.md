# Deployment Instructions

## Custom Domain Setup ✅

The site is configured to use the custom domain: **dzikir.ethiqshub.com**

## What's Already Done:

1. ✅ **Updated Hugo Config**: Set `baseURL = "https://dzikir.ethiqshub.com/"`
2. ✅ **Created CNAME File**: Added `static/CNAME` file with the custom domain
3. ✅ **Tested Build**: Verified that all links work correctly with the new domain
4. ✅ **Added Health Check**: Automated domain health monitoring workflow

## GitHub Pages Configuration Needed:

Since you've already configured Cloudflare to point to `tegarimansyah.github.io`, you just need to:

### Option 1: Via GitHub Web Interface (Recommended)

1. Go to: https://github.com/tegarimansyah/muslim-flashcard/settings/pages
2. Under "Custom domain", enter: `dzikir.ethiqshub.com`
3. Click "Save"
4. Wait for GitHub to verify the domain (this creates a DNS TXT record)
5. Add the TXT record to your Cloudflare DNS settings

### Option 2: Via GitHub CLI

```bash
gh api repos/tegarimansyah/muslim-flashcard/pages -X PUT -f cname=dzikir.ethiqshub.com
```

## Cloudflare Configuration:

Since you mentioned you already added the domain in Cloudflare, ensure:

1. **CNAME Record**: `dzikir.ethiqshub.com` → `tegarimansyah.github.io`
2. **Proxy Status**: Can be either "Proxied" (orange cloud) or "DNS only" (gray cloud)
3. **SSL/TLS Mode**: Set to "Full" or "Full (strict)"

## What This Fixes:

The custom domain configuration solves the original namespace issue where:
- **Before**: Links like `/doa/maksiat-berdosa/` redirected to `https://tegarimansyah.github.io/doa/maksiat-berdosa/`
- **After**: Links now work correctly at `https://dzikir.ethiqshub.com/doa/maksiat-berdosa/`

## Next Steps:

1. Commit and push the changes
2. Enable custom domain in GitHub Pages settings
3. Add the verification TXT record to Cloudflare
4. Test the deployment

The site will be accessible at: **https://dzikir.ethiqshub.com**