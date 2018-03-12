"""Alert when a DUO bypass code is artisanly crafted and not auto-generated."""
from helpers.base import safe_json_loads
from stream_alert.rule_processor.rules_engine import StreamRules

rule = StreamRules.rule


@rule(logs=['duo:administrator'], outputs=['aws-firehose:alerts'])
def duo_bypass_code_create_non_auto_generated(rec):
    """
    author:       @mimeframe
    description:  Alert when a DUO bypass code is artisanly crafted and not auto-generated.
    reference:    https://duo.com/docs/administration-users#generating-a-bypass-code
    """
    return (rec['action'] == 'bypass_create'
            and safe_json_loads(rec['description']).get('auto_generated') is False)
