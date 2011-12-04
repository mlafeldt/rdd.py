#!/bin/sh

test_description="Get metadata of shortened links"

. ./sharness.sh

url="http://www.paulgraham.com/gh.html"
rdd_id="ga4qf47t"

cat >expect <<EOF
{
    "meta": {
        "article": {
            "url": "$url", 
            "title": "Great Hackers", 
            "excerpt": "Want to start a startup? Get funded by Y Combinator . July 2004 (This essay is derived from a talk at Oscon 2004.) A few months ago I finished a new book , and in reviews I keep noticing words like&hellip;", 
            "word_count": 5147, 
            "author": null
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


url="http://the99percent.com/articles/6943/What-Motivates-Us-To-Do-Great-Work"
rdd_id="75x8oaqg"

cat >expect <<EOF
{
    "meta": {
        "article": {
            "url": "$url", 
            "title": "What Motivates Us To Do Great Work? :", 
            "excerpt": "What motivates us to do great work? It s an age-old question. But the age-old answers rewards, recognition, money, stability no longer seem to suffice. As we ve shifted to a knowledge-based economy,&hellip;", 
            "word_count": 667, 
            "author": "Jocelyn K. Glei"
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


url="http://www.inc.com/magazine/20100401/driven-to-distraction.html"
rdd_id="yibs1cca"

cat >expect <<EOF
{
    "meta": {
        "article": {
            "url": "$url", 
            "title": "Driven to Distraction", 
            "excerpt": "Are your business problems making you insane? In his debut column, 37signals co-founder Jason Fried argues that one of the keys to success is to let your lazy side guide you. I think of myself as&hellip;", 
            "word_count": 884, 
            "author": "Jason Fried"
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

test_done
