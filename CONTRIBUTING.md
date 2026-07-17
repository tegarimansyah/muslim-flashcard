# Contribution Guidelines

## Getting Started

Thank you for your interest in contributing to Muslim Flashcard! This project is open-source and welcomes contributions from everyone.

## How to Contribute

### Reporting Issues
- Use the provided GitHub issue templates for bugs, feature requests, or dzikir requests
- Provide clear, detailed information and steps to reproduce
- Include screenshots or screencasts when possible

### Content Contributions
We're always looking to expand our collection of doa and dzikir. You can contribute content by:

1. **Creating a dzikir request issue**: Use the `[DZIKIR]` template to suggest new doa
2. **Direct contribution**: Fork the repository and add new doa to `themes/muslim-flashcard-theme/data/doa.json`

### Code Contributions
- Fork the repository
- Create a feature branch (`git checkout -b feature/amazing-feature`)
- Commit your changes (`git commit -m 'Add amazing feature'`)
- Push to the branch (`git push origin feature/amazing-feature`)
- Open a Pull Request

### Adding New Doa Content

1. Edit `themes/muslim-flashcard-theme/data/doa.json`
2. Add new doa following the existing structure:
```json
{
  "id": "unique-id",
  "title": "Doa Name",
  "arabic": "أَرْبِكُونِي",
  "latin": "Ur biquni",
  "translation": "Translation in Indonesian",
  "background": "Historical context and significance",
  "source": "Qur'an/Hadits reference",
  "category": "category-name"
}
```
3. Update the group information if needed
4. Test locally before pushing

## Development Setup

### Prerequisites
- Hugo Extended v0.133.0 or later
- Node.js (optional, for additional tools)

### Local Development
```bash
# Clone the repository
git clone https://github.com/tegarimansyah/muslim-flashcard.git
cd muslim-flashcard

# Start local development server
./hugo.exe server --buildDrafts --disableFastRender

# Open http://localhost:1313 in your browser
```

## Style Guidelines

### Content
- Use clear, respectful language
- Provide accurate Arabic text with proper diacritics
- Include reliable sources (Qur'an, authentic hadits, etc.)
- Add meaningful context and background information

### Code
- Follow existing code style and conventions
- Use semantic HTML
- Write clean, maintainable JavaScript
- Ensure responsive design works on mobile devices

### Commit Messages
- Use clear, descriptive commit messages
- Prefix with type: `feat:`, `fix:`, `docs:`, `style:`, `refactor:`, `test:`, `chore:`
- Example: `feat: add 3-zone tap areas for story navigation`

## Code Review Process

- All pull requests go through code review
- Be responsive to feedback and suggestions
- Keep discussions constructive and focused
- Address review comments before merging

## Project Structure

```
muslim-flashcard/
├── content/              # Hugo content files
│   ├── pahami/          # Pahami mode pages
│   └── menghafal/       # Menghafal mode pages
├── themes/
│   └── muslim-flashcard-theme/
│       ├── layouts/     # Hugo templates
│       ├── static/      # Static assets (CSS, JS)
│       └── data/        # JSON data files
│           └── doa.json # Main content file
├── .github/
│   └── ISSUE_TEMPLATE/  # GitHub issue templates
└── config.toml          # Hugo configuration
```

## License

This project is open-source. By contributing, you agree that your contributions will be licensed under the same license as the project.

## Questions or Issues?

- Open an issue using the appropriate template
- Join our discussions for community support
- Check existing documentation and FAQs

## Recognition

Contributors will be credited in the project's contributor list. Thank you for helping make Muslim Flashcard better for everyone! 🤲