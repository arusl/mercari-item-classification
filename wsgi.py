from flask_apis import create_app
if __name__ == "__main__":
  app = create_app({'TESTING': True,})
  app.run(host='0.0.0.0', port=5000)