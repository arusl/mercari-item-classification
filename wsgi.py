import os
from flask_apis import create_app

app = create_app({'TESTING': True,})
port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port)