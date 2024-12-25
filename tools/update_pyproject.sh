#!/usr/bin/env bash

OLD_VERSION=$(grep ^version pyproject.toml | cut -d '"' -f 2)
echo "OLD_VERSION: $OLD_VERSION"
OLD_VERSION="\"$OLD_VERSION\""
NEW_VERSION=$(echo "$1" | cut -d '"' -f 2 | cut -d 'v' -f 2)
echo "NEW_VERSION: $NEW_VERSION"
NEW_VERSION="\"$NEW_VERSION\""
sed -i "s+version = $OLD_VERSION+version = $NEW_VERSION+g" pyproject.toml
