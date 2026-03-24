# upkuajing-company-people-search

An AI Agent Skill for querying global corporate business information and personnel data through the UpKuajing Open Platform.

![upkuajing](upkuajing.png)

## Features

- **Company Search**: Search global companies by product, industry, country, size, and more
- **Personnel Search**: Search key personnel by position, company, school, and more
- **Detail Retrieval**: Get corporate business information and detailed personnel resumes
- **Contact Information**: Query emails, phones, WhatsApp, social media, and other contact details

Use cases: Foreign trade customer development, background checks, business negotiation preparation, talent recruitment, competitive analysis.

## Skill Installation

### OpenClaw Installation

1. Copy the entire skill directory to OpenClaw's skills directory:
```bash
cp -r upkuajing-company-people-search ~/.openclaw/workspace/skills/
```

2. Or create a symbolic link:
```bash
ln -s /path/to/upkuajing-company-people-search ~/.openclaw/workspace/skills/
```

3. Restart OpenClaw to activate the skill

### Claude Code Installation

1. Copy the entire skill directory to Claude Code's skills directory:
```bash
cp -r upkuajing-company-people-search ~/.claude/skills/
```

2. Or configure the skills path in Claude Code settings to point to this directory

### Directory Structure Requirements

Ensure the skill directory contains the following structure:
```
upkuajing-company-people-search/
├── SKILL.md              # Skill description file (required)
├── requirements.txt      # Python dependencies
├── scripts/              # Python scripts directory (required)
│   ├── auth.py
│   ├── common.py
│   ├── company_list_search.py
│   ├── human_list_search.py
│   ├── company_details.py
│   ├── human_details.py
│   └── get_contact.py
└── references/           # API reference documentation
    ├── company-list-api.md
    ├── human-list-api.md
    ├── company-detail-api.md
    ├── human-detail-api.md
    └── contact-api.md
```

## Environment Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Set API Key

**Method 1: Using Environment Variables**
```bash
export UPKUAJING_API_KEY=your_api_key_here
```

**Method 2: Using .env File**
```bash
cp .env.example .env
# Edit .env file and fill in your API key
```

### 3. Apply for API Key

If you don't have an API key, you can apply through:
```bash
python scripts/auth.py --new_key
```

## Quick Start

### Using in AI Agent

After installation, you can use it directly in supported AI Agent tools:

**Search Companies**
```
Help me find Chinese manufacturers that produce LED lights with email addresses
```

**Search Personnel**
```
Find the CTO of XXXX
```

**Get Details**
```
Get detailed information for this company: [Company ID]
```

### Command Line Usage

You can also call Python scripts directly:

```bash
# Company list search
python scripts/company_list_search.py \
  --params '{"products": ["LED lights"], "countryCodes": ["CN"], "existEmail": 1}' \
  --query_count 20

# Personnel list search
python scripts/human_list_search.py \
  --params '{"companyNames": ["XXXX"], "titleRoles": ["CTO"]}' \
  --query_count 20

# Get company details
python scripts/company_details.py --pid [Company ID]

# Get personnel details
python scripts/human_details.py --hid [Person ID]

# Get contact information
python scripts/get_contact.py --bus_id [Company or Person ID] --bus_type 1
```

## Usage Examples

### Scenario 1: Foreign Trade Customer Development

Search for US electronics importers:
```bash
python scripts/company_list_search.py \
  --params '{"products": ["electronics"], "countryCodes": ["US"], "existEmail": 1}' \
  --query_count 50
```

### Scenario 2: Background Check

Get detailed information and contact details for target companies:
```bash
# First search for the company
python scripts/company_list_search.py \
  --params '{"companyNames": ["Target Corp"]}' \
  --query_count 10

# Get details
python scripts/company_details.py --pid [Company ID]

# Get contact information
python scripts/get_contact.py --bus_id [Company ID] --bus_type 1
```

### Scenario 3: Talent Recruitment

Find key personnel in specific positions:
```bash
python scripts/human_list_search.py \
  --params '{"titleRoles": ["CEO"], "industries": ["Technology"]}' \
  --query_count 30
```

## API Reference

For detailed API parameter descriptions, please refer to the documentation in the `references/` directory:
- [Company List Search](references/company-list-api.md)
- [Personnel List Search](references/human-list-api.md)
- [Company Details](references/company-detail-api.md)
- [Personnel Details](references/human-detail-api.md)
- [Contact Information](references/contact-api.md)

## Pricing

All API calls incur fees. For latest pricing, please visit: https://www.upkuajing.com/openapi/pricing

**Reference Prices:**
- Company list search: 0.5 CNY/request (max 20 records per request)
- Personnel list search: 0.2 CNY/request (max 20 records per request)
- Company details: 0.5 CNY/request
- Personnel details: 0.2 CNY/request
- Contact information: 1 CNY/request

**Account Recharge:**
```bash
python scripts/auth.py --new_rec_order
```

## Troubleshooting

### Invalid API Key
Check if the API key in environment variables or .env file is correctly set.

### Insufficient Balance
Run `python scripts/auth.py --account_info` to check account balance and recharge if needed.

### Permission Error
Confirm that your API key has access to the relevant API endpoints.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Support

For questions or suggestions, please submit an Issue or Pull Request.
