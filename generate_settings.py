import os, re

def create_proxy_config(schema, host, port):
  return f"""
    <proxy>
      <id>{schema}-proxy</id>
      <active>true</active>
      <protocol>{schema}</protocol>
      <host>{host}</host>
      <port>{port}</port>
      <nonProxyHosts>localhost</nonProxyHosts>
    </proxy>
  """


def main():
  proxy_confs = ""
  # for http_proxy
  http_proxy_url = os.getenv("http_proxy")
  if http_proxy_url:
    match = re.search("http://(.+):(\d+)", http_proxy_url)
    http_host, http_port = match.group(1), match.group(2)
    http_proxy_conf = create_proxy_config("http", http_host, http_port)
    proxy_confs += http_proxy_conf
    
  # for https_proxy
  https_proxy_url = os.getenv("https_proxy")
  if https_proxy_url:
    match = re.search("http://(.+):(\d+)", https_proxy_url)
    https_host, https_port = match.group(1), match.group(2)
    https_proxy_conf = create_proxy_config("http", https_host, https_port)
    proxy_confs += https_proxy_conf

  if proxy_confs:
    print(f"""
<settings>
  <proxies>
    {proxy_confs}
  </proxies>
</proxies>
    """.lstrip())
  else:
    print(f"""
<settings>
  <proxies/>
</proxies>
    """.lstrip())
  
if __name__ == "__main__":
  main()