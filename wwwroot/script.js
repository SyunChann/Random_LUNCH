const { createApp } = Vue;

createApp({
  data() {
    return {
      menus: [],
      selectedMenu: null,
    };
  },
  mounted() {
    // 서버에서 엑셀 파일 데이터를 로드
    axios.get('/api/LunchMenu')
      .then(response => {
        this.menus = response.data;
      })
      .catch(error => {
        console.error("메뉴를 불러오는 중 오류 발생:", error);
      });
  },
  methods: {
    spin() {
      if (this.menus.length > 0) {
        const randomIndex = Math.floor(Math.random() * this.menus.length);
        this.selectedMenu = this.menus[randomIndex];
      }
    }
  }
}).mount('#app');