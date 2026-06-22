#! /bin/bash

#! /bin/bash

set -e -o pipefail -x

LOG_FILE="/tmp/install-packages.log"
exec > >(tee -a "$LOG_FILE") 2>&1

cd "$(dirname "$0")"

# Switch to nftables to avoid iptables errors in Docker.
# This fixes "Table does not exist (do you need to insmod?)" errors when starting dockerd.
sudo update-alternatives --set iptables /usr/sbin/iptables-nft
sudo service docker stop || true
sudo pkill -x dockerd || true
sudo pkill -x containerd || true
sudo /usr/local/share/docker-init.sh

# Install Google Antigravity CLI
curl -fsSL https://antigravity.google/cli/install.sh | bash

# Install npm tools
npm install -g --no-fund \
    @bitwarden/cli@2026.5.0 \
    markdownlint-cli2@0.22.1 \
    @playwright/cli@0.1.13

npx -y playwright@1.60.0 install --with-deps

# shellcheck disable=SC2043
for pkg in ruff; do
   uv tool install $pkg;
done


# # Install skills
# # https://skills.sh/
# # https://github.com/vercel-labs/skills
# for skill in \
#     "coderabbitai/skills@autofix" \
#     "coderabbitai/skills@code-review" \
#     "JohnStrunk/skills@ears-gherkin-dev" \
#     "upstash/context7@find-docs" \
# ; do
#     source="$(echo "$skill" | cut -d '@' -f 1)"
#     skillname="$(echo "$skill" | cut -d '@' -f 2)"
#     ( cd .. && \
#     npx -y skills install "$source" --yes \
#         --agent claude-code \
#         --agent opencode \
#         --skill "$skillname"
#     )
# done
