function sendRequest(method: string, url: string, data={}): string {
   const xhr = new XMLHttpRequest();
   xhr.open(method, url, false);
   xhr.setRequestHeader('Content-Type', 'application/json');
   xhr.send(JSON.stringify(data));
   if (xhr.status === 200) {
      return xhr.responseText;
   } else {
      throw new Error('Request failed: ' + xhr.statusText);
   }
}