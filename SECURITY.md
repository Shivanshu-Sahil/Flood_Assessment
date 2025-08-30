# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |

## Reporting a Vulnerability

If you discover a security vulnerability, please send an email to [your-email@example.com]. All security vulnerabilities will be promptly addressed.

Please include the following information in your report:
- Description of the vulnerability
- Steps to reproduce
- Potential impact
- Suggested fix (if any)

## Security Best Practices

When using this application:

1. **API Keys**: Never commit API keys to version control
2. **Environment Variables**: Always use environment variables for sensitive data
3. **File Uploads**: The system validates file types and sizes, but always review uploaded content
4. **CORS**: Configure CORS appropriately for your deployment environment
5. **HTTPS**: Use HTTPS in production deployments

## Dependencies

We regularly update dependencies to address security vulnerabilities. Please keep your installation up to date.
