import web
import twitter_sense_v2

urls = (
    '/', 'index'
)

class index:
    def GET(self):
	get_input = web.input(_method='get')
	print get_input.q
	return str(twitter_sense_v2.main(get_input.q))

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()

