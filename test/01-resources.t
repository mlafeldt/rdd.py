#!/bin/sh
# vi: set ft=sh :

test_description="Get information about sub-resources"

. ./sharness.sh

unset RDD_URL
unset RDD_VERBOSE
test "$verbose" = "t" && export RDD_VERBOSE=1


cat >expect <<EOF
urls/:id:
  href:
    /api/shortener/v1/urls/:id
  description:
    The URL endpoint. GET a URL ID to view available metadata of a shortened link.
urls:
  href:
    /api/shortener/v1/urls
  description:
    The URLs endpoint. POST a URL to add it to the shortener.
EOF

test_expect_success "$test_description" "
    rdd_r resources >result &&
    test_cmp expect result
"

test_done
