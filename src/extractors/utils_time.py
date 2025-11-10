thonfrom dateutil import parser

def parse_timestamp(timestamp_str):
    try:
        dt = parser.parse(timestamp_str)
        return dt.isoformat()
    except Exception:
        return None