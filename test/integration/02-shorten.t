#!/bin/sh
# vi: set ft=sh :

test_description="Create shortened URLs"

SHARNESS_BUILD_DIRECTORY="$PWD/../.."

. ./sharness.sh

unset RDD_URL
unset RDD_VERBOSE
test "$verbose" = "t" && export RDD_VERBOSE=1


shorten() {
    url="$1"
    rdd_id="$2"

    cat >expect <<EOF
url:
  /api/shortener/v1/urls/$rdd_id
rdd_url:
  http://rdd.me/$rdd_id
id:
  $rdd_id
EOF

    test_expect_success "Shorten URL $url ($rdd_id)" "
        rdd_r shorten $url >result &&
        test_cmp expect result
    "
}

shorten "http://www.paulgraham.com/gh.html" "ga4qf47t"
shorten "http://the99percent.com/articles/6943/What-Motivates-Us-To-Do-Great-Work" "75x8oaqg"
shorten "http://www.inc.com/magazine/20100401/driven-to-distraction.html" "yibs1cca"
shorten "http://www.forbes.com/sites/venkateshrao/2011/12/05/the-rise-of-developeronomics/" "c1xma652"
shorten "http://lubutu.com/idea/ivo" "vqvvpmhg"

test_done
