new Vue({
    el: '#tweets',
    data() {
        return {
            tweets: [],
            form: {
                name: '',
                message: ''
            }
        }
    },
    methods: {
        loadTweets() {

            fetch('/tweets').then(data=> data.json()).then(tweets=> {
                this.tweets = tweets;
            })

        },
        addTweet(evt) {
            evt.preventDefault();

            fetch('/tweets', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    name: this.form.name,
                    message: this.form.message
                })
            }).then(_=> {
                this.form.name = '';
                this.form.message = '';
                this.loadTweets()
            });

        }
    },
    mounted() {
        this.loadTweets()
    }
})