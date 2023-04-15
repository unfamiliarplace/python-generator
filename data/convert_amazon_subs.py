# This script allows you modify a subtitle file by a given offset.

# IMPORTS

import re

# CONSTANTS

# Example line: 00:00:33,159 --> 00:00:35,999
MARKER      = '-->'
MIN         = 60000
HR          = 60 * MIN
TS          = r'<p begin="(.*?)" end="(.*?)" region="AmazonDefaultRegion" style="AmazonDefaultStyle">(.*?)</p>'

# WORKING WITH TIMESTAMPS

def parse_ts(ts: str) -> int:
    """Return the number of milliseconds in a given timestamp."""

    # Get the separate parts
    hrs, mins, ms = ts.split(':')
    ms = ms.replace('.', '')

    # Turn them into a single int
    ms = int(ms)
    ms += int(mins) * MIN
    ms += int(hrs) * HR

    return ms


def format_ts(ms: int) -> str:
    """Format the given milliseconds as a timestamp."""

    hrs = 0
    mins = 0

    # Count hours
    while ms > HR:
        ms -= HR
        hrs += 1

    # Count minutes
    while ms > MIN:
        ms -= MIN
        mins += 1

    # Format
    ts = '{}:{}:{}'.format(
        str(hrs).zfill(2),
        str(mins).zfill(2),
        str(ms).zfill(5)
    )

    ts = ts[:-3] + ',' + ts[-3:]
    return ts

def format_sub(start, end, sub) -> str:
    """Return a formatted subtitle."""

    sub = sub.replace('<br />', '\n')
    if sub.startswith("'") and sub.endswith("'"):
        sub = f'<i>{sub[1:-1]}</i>'

    start = format_ts(parse_ts(start))
    end = format_ts(parse_ts(end))

    return f'{start} --> {end}\n{sub}'

# WORKING WITH LINES

def convert_line(line: str) -> str:
    match = re.search(TS, line)
    if match:
        start, end, sub = match.group(1), match.group(2), match.group(3)
        return format_sub(start, end, sub)    

def convert_lines(lines: list) -> iter:
    i = 1
    for line in lines:
        conv = convert_line(line)
        if conv:
            yield f'{i}\n{conv}'
            i += 1

# RUNNING

def prompt_fname() -> str:
    """Return a str (filename)."""

    fname = input('Enter the name of a subtitle file: ').strip()
    return fname

def prompt_offset() -> int:
    """Return an int (milliseconds offset)."""

    offset = int(input('Enter an offset in milliseconds: ').strip())
    return offset

def get_fix_fname(fname: str) -> str:
    """Return the filename for the fixed version."""
    
    return f'{fname[:fname.rfind(".")]}_fix.srt'
    

def run() -> None:
    """Open file, correct each line, save to new file."""

    # Determine filenames and offset
    fname = prompt_fname()
    fname_fix = get_fix_fname(fname)

    with open(fname, 'r') as f, open(fname_fix, 'w') as f_fix:
        lines = convert_lines(f.readlines())
        f_fix.write('\n\n'.join(lines))

    # Report 
    input('Saved to {}\nPress Enter to quit.'.format(fname_fix))


# PROGRAM

if __name__ == '__main__':
    run()
