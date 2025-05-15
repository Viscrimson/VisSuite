import argparse
from registry import save_tokens, load_tokens
from cache_link import ensure_link
from launcher import launch

parser = argparse.ArgumentParser()
sub = parser.add_subparsers(dest='cmd')

# init
i = sub.add_parser('init')
i.add_argument('account')
# launch
l = sub.add_parser('launch')
l.add_argument('account')
args = parser.parse_args()

if args.cmd == 'init':
    load_tokens(args.account)  # ensure fresh state
    launch_account(args.account)
    save_tokens(args.account)
elif args.cmd == 'launch':
    save = load_tokens(args.account)
    ensure_cache_links(args.account)
    launch_account(args.account)