#!/bin/sh

test_description="Get metadata of shortened links"

. ./sharness.sh

json_str() {
    test -n "$1" && echo -n \"$1\" || echo -n null
}

metadata() {
    url="$1"
    title=$(json_str "$2")
    excerpt=$(json_str "$3")
    words="$4"
    author=$(json_str "$5")
    rdd_id="$6"

    cat >expect <<EOF
{
    "meta": {
        "article": {
            "url": "$url", 
            "title": $title, 
            "excerpt": $excerpt, 
            "word_count": $words, 
            "author": $author
        }, 
        "rdd_url": "http://rdd.me/$rdd_id", 
        "id": "$rdd_id", 
        "full_url": "http://readability.com/articles/$rdd_id"
    }, 
    "messages": [
        "Article found."
    ], 
    "success": true
}
EOF

    test_expect_success "Get metadata of $rdd_id ($url)" "
        rdd_r metadata $rdd_id >result &&
        test_cmp expect result
    "
}

metadata "http://www.paulgraham.com/gh.html" \
    "Great Hackers" \
    "Want to start a startup? Get funded by Y Combinator . July 2004 (This essay is derived from a talk at Oscon 2004.) A few months ago I finished a new book , and in reviews I keep noticing words like&hellip;" \
    5147 \
    "" \
    ga4qf47t

metadata "http://the99percent.com/articles/6943/What-Motivates-Us-To-Do-Great-Work" \
    "What Motivates Us To Do Great Work? :" \
    "What motivates us to do great work? It s an age-old question. But the age-old answers rewards, recognition, money, stability no longer seem to suffice. As we ve shifted to a knowledge-based economy,&hellip;" \
    667 \
    "Jocelyn K. Glei" \
    75x8oaqg

metadata "http://www.inc.com/magazine/20100401/driven-to-distraction.html" \
    "Driven to Distraction" \
    "Are your business problems making you insane? In his debut column, 37signals co-founder Jason Fried argues that one of the keys to success is to let your lazy side guide you. I think of myself as&hellip;" \
    884 \
    "Jason Fried" \
    yibs1cca

test_done
