#!/bin/sh
# vi: set ft=sh :

test_description="Get metadata of shortened links"

SHARNESS_BUILD_DIRECTORY="$PWD/../.."

. ./sharness.sh

unset RDD_URL
unset RDD_VERBOSE
test "$verbose" = "t" && export RDD_VERBOSE=1


metadata() {
    rdd_id="$1"
    url="$2"
    title="$3"
    excerpt="$4"
    words="$5"
    author="${6:-None}"

    cat >expect <<EOF
article:
  url:
    $url
  title:
    $title
  excerpt:
    $excerpt
  word_count:
    $words
  author:
    $author
rdd_url:
  http://rdd.me/$rdd_id
id:
  $rdd_id
full_url:
  http://readability.com/articles/$rdd_id
EOF

    test_expect_success "Get metadata of $rdd_id ($url)" "
        rdd_r metadata $rdd_id >result &&
        test_cmp expect result
    "
}

metadata "ga4qf47t" \
    "http://www.paulgraham.com/gh.html" \
    "Great Hackers" \
    "Want to start a startup? Get funded by Y Combinator. July 2004(This essay is derived from a talk at Oscon 2004.)A few months ago I finished a new book, and in reviews I keep noticing words like&hellip;" \
    5147 \
    ""

metadata "75x8oaqg" \
    "http://the99percent.com/articles/6943/What-Motivates-Us-To-Do-Great-Work" \
    "What Motivates Us To Do Great Work? :" \
    "What motivates us to do great work? It s an age-old question. But the age-old answers rewards, recognition, money, stability no longer seem to suffice. As we ve shifted to a knowledge-based economy,&hellip;" \
    674 \
    "Jocelyn K. Glei"

metadata "yibs1cca" \
    "http://www.inc.com/magazine/20100401/driven-to-distraction.html" \
    "Driven to Distraction" \
    "Are your business problems making you insane? In his debut column, 37signals co-founder Jason Fried argues that one of the keys to success is to let your lazy side guide you. Jason Fried is the&hellip;" \
    900 \
    ""

metadata "c1xma652" \
    "http://www.forbes.com/sites/venkateshrao/2011/12/05/the-rise-of-developeronomics/" \
    "The Rise of Developeronomics" \
    "There is a theory in evolutionary biology that reciprocal altruism and cooperation first appeared as a solution to the food storage problem. If you were an early hominid and you killed a large&hellip;" \
    783 \
    ""

metadata "vqvvpmhg" \
    "http://lubutu.com/idea/ivo" \
    "Ivo." \
    "A teletype no more Incredible effort has been put into interaction design recently. Unfortunately, all that effort has been targeted towards inexperienced users, pretty much ignoring those of us who&hellip;" \
    1935 \
    ""

test_done
