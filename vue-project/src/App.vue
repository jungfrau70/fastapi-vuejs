<template>
  <div>
    <h1>Signals</h1>
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>Market</th>
          <th>Symbol</th>
          <th>Datetime</th>
          <th>Buy Position</th>
          <th>Current Price</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in stockData" :key="item.id">
          <td>{{ item.id }}</td>
          <td>{{ item.market }}</td>
          <td>{{ item.sym }}</td>
          <td>{{ formatDatetime(item) }}</td>
          <td>{{ item.buy_position || 'N/A' }}</td>
          <td>{{ item.current_price }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  data() {
    return {
      stockData: [],
    };
  },
  mounted() {
    this.connectToSSE();
  },
  methods: {
    connectToSSE() {
      const eventSource = new EventSource('http://localhost:8000/stream'); // Update with your SSE endpoint URL

      eventSource.addEventListener('new_message', (event) => {
        const message = JSON.parse(event.data);

        // Update the stockData array with the new data
        this.stockData = message;
      });

      eventSource.onerror = (error) => {
        console.error('SSE Error:', error);
      };
    },
    formatDatetime(item) {
      let date = new Date(item.datetime);

      // Add 15 hours to the date
      date.setHours(date.getHours() + 15);

      return date.toLocaleString('en-US', { timeZone: 'Asia/Seoul' });
    }

  },
};
</script>

<style scoped>
/* Add your CSS styles here */
</style>
