import speedtest

st = speedtest.Speedtest()

download_speed = st.download()

upload_speed = st.upload()

print(f"Download speed: {download_speed / 1e+6} Mbps")
print(f"Upload speed: {upload_speed / 1e+6} Mbps")
