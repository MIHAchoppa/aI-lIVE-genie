# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |

## Security Best Practices

### API Key Management

1. **Never commit API keys to source control**
   - Always use environment variables
   - Use `.env` files (excluded via .gitignore)
   - Rotate keys regularly

2. **Production Deployment**
   - Always change the default API key
   - Use strong, randomly generated keys
   - Set `AI_GENIE_API_KEY` environment variable
   - Never use the default `dev-key-change-in-production`

3. **API Key Logging**
   - The application intentionally does NOT log actual API keys
   - Only status messages are logged (e.g., "Custom key configured")
   - CodeQL may flag these as potential issues, but they are false positives

### Data Storage

1. **Data Directory Security**
   - Data is stored in `data/` directory (excluded from git)
   - Files contain: conversation history, goals, preferences
   - Ensure proper file system permissions (chmod 600 recommended)
   - Back up data regularly

2. **Sensitive Information**
   - Don't store passwords or tokens in the memory system
   - Be cautious about storing PII (Personally Identifiable Information)
   - Consider encrypting sensitive data before storage

### API Server Security

1. **Network Security**
   - Use HTTPS in production (terminate SSL at reverse proxy)
   - Implement rate limiting
   - Use firewall rules to restrict access
   - Consider IP whitelisting for sensitive deployments

2. **CORS Configuration**
   - Default: allows all origins (development mode)
   - Production: configure specific allowed origins in api_server.py
   - Example:
     ```python
     CORS(app, resources={
         r"/api/*": {
             "origins": ["https://yourdomain.com"]
         }
     })
     ```

3. **Input Validation**
   - API validates required parameters
   - Type checking on inputs
   - Consider additional validation for production use

### GitHub Actions Workflow Security

- Workflows use minimal permissions (`contents: read`)
- No secrets are logged or exposed
- Dependencies are pinned to specific versions

## Security Audit Results

### CodeQL Analysis (October 2025)

**Findings:**
1. ✅ **GitHub Actions Permissions**: Fixed - workflows now use explicit minimal permissions
2. ⚠️ **API Key Logging**: False positive - application logs only status messages, never actual keys

**Explanation of False Positive:**
The static analysis tool detects data flow from API key environment variables to print statements. However, the actual logging only outputs status messages like "Custom key configured" or "Using default dev key", never the actual key value. This is by design and is a false positive.

### Known Security Considerations

1. **Data Storage**: Files stored in plain JSON
   - Consider encryption at rest for sensitive deployments
   - File system permissions are user's responsibility

2. **No Built-in Encryption**: Core library doesn't encrypt data
   - Users can implement encryption layer if needed
   - Consider using system-level encryption (LUKS, BitLocker)

3. **API Authentication**: Simple API key authentication
   - Suitable for personal/small team use
   - Production deployments may want OAuth2/JWT
   - Consider adding API key rotation mechanism

## Reporting a Vulnerability

If you discover a security vulnerability, please follow these steps:

1. **Do NOT open a public issue**
2. Email the maintainer directly (see GitHub profile)
3. Include:
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fix (if any)

We aim to respond within 48 hours and provide a fix within 7 days for critical issues.

## Security Checklist for Production

- [ ] Change default API key to a strong random value
- [ ] Set API key via environment variable
- [ ] Use HTTPS (reverse proxy with SSL termination)
- [ ] Configure CORS for specific origins only
- [ ] Implement rate limiting
- [ ] Set up firewall rules
- [ ] Restrict file system permissions on data directory
- [ ] Enable audit logging
- [ ] Regular security updates
- [ ] Regular data backups
- [ ] Monitor for suspicious activity

## Additional Resources

- [OWASP API Security Top 10](https://owasp.org/www-project-api-security/)
- [Flask Security Best Practices](https://flask.palletsprojects.com/en/2.3.x/security/)
- [Python Security Guide](https://python.readthedocs.io/en/latest/library/security_warnings.html)

## Updates

This security policy is reviewed and updated quarterly. Last update: October 2025
