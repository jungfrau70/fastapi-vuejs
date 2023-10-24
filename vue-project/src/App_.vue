<!-- <template>
  <div>
    <h1>Real-Time Data</h1>
    <ul>
      <li v-for="message in messages" :key="message.id">
        <strong>Event:</strong> {{ message.event }}
        <pre><code>{{ message.data }}</code></pre>
      </li>
    </ul>
  </div>
  <div>
    <DataTable class="display">
    <thead>
      <li v-for="message in messages" :key="message.id">
        <tr>
            <th>{{ message.data[0].id }}</th>
            <th>{{ message.data[0].market }}</th>
        </tr>
      </li>
    </thead>
</DataTable>
  </div>
</template> -->
<template>
  <div id="app">
    {{ answer }}
  </div>
</template>

<script>
export default {
  name: "App",
  data() {
    return {
      answer: {},
      timer: "",
    };
  },
  created() {
    this.fetchData();
    this.timer = setInterval(this.fetchData, 5000);
  },
  methods: {
    async fetchData() {
      // const res = await fetch("https://yesno.wtf/api");
      const res = new EventSource('http://localhost:8000/stream');
      const data = await res.json();
      this.answer = data;
    },
    cancelAutoUpdate() {
      clearInterval(this.timer);
    },
  },
  beforeDestroy() {
    this.cancelAutoUpdate();
  },
};
</script>
<!-- 
  created() {
    this.connectToSSE();
    this.timer = setInterval(this.fetchData, 5000);
  },
  methods: {
    connectToSSE() {
      // Replace with your SSE endpoint URL
      // const eventSource = new EventSource('http://localhost:8000/stream', { withCredentials: true });
      const eventSource = new EventSource('http://localhost:8000/stream');

      eventSource.addEventListener('new_message', (event) => {
        const message = JSON.parse(event.data);
        // console.log(message)
        this.messages.push({
          id: event.lastEventId,
          event: event.type,
          data: message,
        });

        // Log the received data to the browser console
        console.log('Received data:', message);
      });

      eventSource.onerror = (error) => {
        console.error('SSE Error:', error);
      };
    },
    cancelAutoUpdate() {
      clearInterval(this.timer);
    },
  },
  beforeDestroy() {
    this.cancelAutoUpdate();
  },
};
</script> -->