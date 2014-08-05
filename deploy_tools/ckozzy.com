server {
	listen 80;
	server_name ckozzy.com;

	location /static  {
		alias /home/ozzy/sites/ckozzy.com/static;
	}
	location / {
		proxy_set_header Host $host;
		#proxy_pass http://unix:/tmp/ckozzy.com.socket;
		proxy_pass http://localhost:8000;
	}
}
