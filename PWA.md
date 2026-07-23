# PWA Implementation Guide

## Overview
Dzikir with EthiqsHub is now a Progressive Web App (PWA) that can be installed on mobile devices and works offline.

## PWA Features

### ✅ Implemented
- **Manifest File**: `static/manifest.json` - App metadata and icons
- **Service Worker**: `static/sw.js` - Offline functionality and caching
- **Responsive Icons**: 8 sizes (72x72 to 512x512) + favicon + apple-touch-icon
- **Theme Colors**: Islamic green (#059669) for browser UI
- **Install Prompt**: "Add to Home Screen" on mobile devices
- **Offline Support**: Core pages cached and available offline
- **App-like Experience**: Standalone mode without browser UI

## How to Install

### On Android (Chrome)
1. Open https://dzikir.ethiqshub.com in Chrome
2. Tap the menu (⋮) → "Add to Home screen" or "Install app"
3. Confirm installation
4. App icon appears on home screen

### On iOS (Safari)
1. Open https://dzikir.ethiqshub.com in Safari  
2. Tap Share button (↑) → "Add to Home Screen"
3. Confirm installation
4. App icon appears on home screen

### On Desktop (Chrome/Edge)
1. Open https://dzikir.ethiqshub.com
2. Look for install icon (⊕) in address bar
3. Click "Install"
4. App appears in applications/start menu

## Technical Details

### Manifest File
```json
{
  "name": "Dzikir with EthiqsHub",
  "short_name": "Dzikir",
  "start_url": "/",
  "display": "standalone",
  "theme_color": "#059669",
  "icons": [...]
}
```

### Service Worker Strategy
- **Cache First**: Static assets served from cache
- **Network First**: Dynamic content fetched from network, then cached
- **Offline Fallback**: Returns homepage if network fails

### Icon Generation
Icons generated programmatically using `generate-icons.py`:
- Islamic green gradient background
- Geometric book/reading symbol
- Arabic letter "ذ" (Dz) for branding
- All standard PWA sizes supported

## Testing PWA

### Chrome DevTools
1. Open DevTools (F12)
2. Go to "Application" tab
3. Check "Manifest" - should show app details
4. Check "Service Workers" - should be active and running
5. Check "Storage" - should show cached resources

### Lighthouse
1. Open DevTools → Lighthouse
2. Select "Progressive Web App"  
3. Run audit
4. Should pass all PWA criteria

### Offline Testing
1. Open DevTools → Network tab
2. Check "Offline" checkbox
3. Reload page
4. Core functionality should still work

## File Structure

```
static/
├── manifest.json          # PWA manifest
├── sw.js                  # Service worker
├── robots.txt            # SEO + sitemap
├── favicon.ico           # Browser tab icon
├── apple-touch-icon.png  # iOS home screen
└── icons/
    ├── icon-72x72.png
    ├── icon-96x96.png
    ├── icon-128x128.png
    ├── icon-144x144.png
    ├── icon-152x152.png
    ├── icon-192x192.png
    ├── icon-384x384.png
    └── icon-512x512.png
```

## Configuration

### Hugo Config
```toml
[params.pwa]
  enabled = true
  manifest = "/manifest.json"
  serviceWorker = "/sw.js"
```

### HTML Head
```html
<link rel="manifest" href="/manifest.json">
<meta name="theme-color" content="#059669">
<meta name="apple-mobile-web-app-capable" content="yes">
```

### Service Worker Registration
```javascript
if ('serviceWorker' in navigator) {
  navigator.serviceWorker.register('/sw.js')
    .then(reg => console.log('SW registered'))
    .catch(err => console.log('SW failed'));
}
```

## Deployment

### GitHub Pages
- All PWA files in `static/` are served directly
- Service worker scope is root `/`
- HTTPS required (automatic with GitHub Pages)

### Domain Configuration
- Works with custom domain: `dzikir.ethiqshub.com`
- Manifest URLs use relative paths for flexibility

## Troubleshooting

### Service Worker Not Registering
- Check browser console for errors
- Ensure HTTPS is enabled
- Verify `sw.js` is accessible at `/sw.js`

### Icons Not Showing
- Clear browser cache
- Verify icon files exist in `static/icons/`
- Check manifest paths are correct

### Install Prompt Not Showing
- Must visit site multiple times (engagement requirement)
- Ensure HTTPS is enabled
- Check manifest is valid (DevTools → Application → Manifest)

### Offline Not Working
- Verify service worker is active
- Check cache storage in DevTools
- Ensure cache strategy matches your needs

## Performance Benefits

### Faster Load Times
- Static assets cached locally
- No network requests for cached content
- Instant page transitions

### Reduced Bandwidth
- Only new/changed content downloaded
- Core functionality available offline
- Better experience on slow connections

### Improved Engagement
- App-like experience increases usage
- Home screen icon for easy access
- Push notifications potential (future)

## Future Enhancements

### Planned Features
- [ ] Push notifications for daily amalan
- [ ] Background sync for favorites
- [ ] Offline-first data storage
- [ ] Periodic content updates
- [ ] Share functionality

### Considerations
- Cache size limits (quota management)
- Service worker update strategy
- Offline analytics tracking
- Cross-browser compatibility

## Resources

- [PWA Best Practices](https://web.dev/progressive-web-apps/)
- [Service Worker API](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API)
- [Web App Manifest](https://developer.mozilla.org/en-US/docs/Web/Manifest)
- [Lighthouse PWA Checklist](https://web.dev/lighthouse-pwa/)

---

**Note**: This PWA implementation follows Google's PWA criteria and should pass all Lighthouse PWA audits.