<template>
  <div>

    <div class="map-container">
      <div class="map-wrapper">
        <div id="map"></div>
      </div>

      <div class="controls-wrapper">
        <div class="controls-box">
          <select v-model="selectedSido" class="custom-select" style="width:120px;">
            <option v-for="(item, idx) in sido" :key="idx" :value="item">{{ item }}</option>
          </select>
          <select v-model="selectedSigungu" class="custom-select">
            <option v-for="(item, idx) in sigunguSelect" :key="idx" :value="item">{{ item }}</option>
          </select>
          <select v-model="searchbank" class="custom-select"  style="width:230px;">
            <option v-for="(item, idx) in bankList" :key="idx" :value="item">{{ item }}</option>
          </select>

          <div class="search-bar">
            <button class="btn btn-outline-dark" @click="searchLocation">검색</button>
          </div>
        </div>
      </div>
    </div>

    <!--인포윈도우 클릭 시 나오는 모달 창-->
    <div>
      <div v-if="showModal" class="modal">
        <div class="modal-content">
          <p>이름 : {{ selectedPlace.place_name }}</p>
          <p>도로명 주소 : {{ selectedPlace.road_address_name }}</p>
          <p>자세히보기: <a :href="selectedPlace.place_url">{{ selectedPlace.place_url }}</a> </p>

          <button class="btn btn-outline-dark" @click="closeModal">Close</button>
        </div>
      </div>
    </div>

  </div>


</template>

<script>
export default {
  name: "KakaoMap",
  data() {
    return {
      apiKey: '6431aa53a46e78d2c2d5dd9b08c5bdeb',
      searchbank: this.$store.state.searchmap.bankname, // 검색어를 저장할 데이터
      markers: [],
      infowindow: null,
      sido: this.$store.state.searchmap.sidoSelect,
      bankList: this.$store.state.searchmap.bankSelect,
      selectedSido: '서울',
      selectedSigungu: '전체',
      selectedPlace: null,
      showModal: false
    };
  },
  mounted() {
    if (window.kakao && window.kakao.maps) {
      this.initMap();
      this.searchLocation();
    } else {
      const script = document.createElement("script");
      /* global kakao */
      script.onload = () => {
        kakao.maps.load(() => {
          this.initMap();
          this.searchLocation();
        });
      };
      script.src =
          `//dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=${this.apiKey}&libraries=services`;
      document.head.appendChild(script);
    }
  },
  computed: {
    searchQuery(){
      let sido = ''
      let sigungu = ''
      if (this.selectedSido === '전체'){
        sido = ''
      } else{
        sido = this.selectedSido
      }
      if (this.selectedSigungu === '전체'){
        sigungu = ''
      } else{
        sigungu = this.selectedSigungu
      }

      return `${sido} ${sigungu} ${this.searchbank}`
    },

    sigunguSelect() {

      const sigunguList = this.$store.state.searchmap.sigunguSelect
      for (let i of sigunguList) {
        const [key,value] = Object.entries(i)
        console.log(value)
        if (key[0] === this.selectedSido) {
          return key[1]
        }
      }
      return null
    }

  },
  methods: {
    initMap() {
      const container = document.getElementById("map");
      const options = {
        center: new kakao.maps.LatLng(33.450701, 126.570667),
        level: 5,
      };

      //지도 객체를 등록합니다.
      //지도 객체는 반응형 관리 대상이 아니므로 initMap에서 선언합니다.
      this.map = new kakao.maps.Map(container, options);
    },
    displayInfoWindow() {
      if (this.infowindow && this.infowindow.getMap()) {
        //이미 생성한 인포윈도우가 있기 때문에 지도 중심좌표를 인포윈도우 좌표로 이동시킨다.
        this.map.setCenter(this.infowindow.getPosition());
        return;
      }

      var iwContent = '<div style="padding:5px;">Hello World!</div>', // 인포윈도우에 표출될 내용으로 HTML 문자열이나 document element가 가능합니다
          iwPosition = new kakao.maps.LatLng(33.450701, 126.570667), //인포윈도우 표시 위치입니다
          iwRemoveable = true; // removeable 속성을 ture 로 설정하면 인포윈도우를 닫을 수 있는 x버튼이 표시됩니다

      this.infowindow = new kakao.maps.InfoWindow({
        map: this.map, // 인포윈도우가 표시될 지도
        position: iwPosition,
        content: iwContent,
        removable: iwRemoveable,
      });

      this.map.setCenter(iwPosition);
    },
    searchLocation() {
      if (this.searchQuery === "") {
        return; // 검색어가 비어있으면 종료
      }

      const places = new kakao.maps.services.Places();
      places.keywordSearch(this.searchQuery, (result, status) => {
        if (status === kakao.maps.services.Status.OK) {
          // 검색 결과를 모두 표시하는 범위를 생성합니다.
          const bounds = new kakao.maps.LatLngBounds();

          // 기존 마커들 제거
          if (this.markers.length > 0) {
            this.markers.forEach((marker) => {
              marker.setMap(null);
              marker.infowindow.close();
            });
            this.markers = [];
          }

          // 검색한 모든 장소에 대해 마커와 인포윈도우 생성
          result.forEach((place) => {
            const position = new kakao.maps.LatLng(place.y, place.x);

            // 마커 생성
            const marker = new kakao.maps.Marker({
              map: this.map,
              position: position,
            });
            this.markers.push(marker);

            // 인포윈도우 생성
            const infowindow = new kakao.maps.InfoWindow({
              content: place.place_name, // 인포윈도우에 표시할 내용
            });
            marker.infowindow = infowindow; // 마커 객체에 인포윈도우 저장

            // 마커에 마우스 이벤트 추가
            kakao.maps.event.addListener(marker, "mouseover", () => {
              infowindow.open(this.map, marker); // 마우스를 올릴 때 인포윈도우 오픈
            });
            kakao.maps.event.addListener(marker, "mouseout", () => {
              infowindow.close(); // 마우스를 내릴 때 인포윈도우 닫기
            });
            kakao.maps.event.addListener(marker, "click", () => {
              this.selectedPlace = place; // 선택된 장소를 저장
              this.showModal = true; // 모달창 표시
            });

            // 범위에 마커 포함
            bounds.extend(position);
          });

          // 지도 중심 이동 및 확대/축소 레벨 조정
          this.map.setBounds(bounds);
        } else {
          // 검색 실패 처리
          alert('검색 결과가 없습니다.')
        }
      });
    },
    closeModal(){
      this.showModal = false
    },

  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#map {
  width: 100%;
  height: 100%;
}


.map-container {
  position: relative;
}

.map-wrapper {
  width: 100%;
  height: 100vh;
}

.controls-wrapper {
  position: absolute;
  top: 10px;
  left: 10px;
  z-index: 100;
  background-color: rgba(255, 255, 255, 0.9);
}

.controls-box {
  display: flex;
  gap: 10px;
  padding: 10px;
}

.search-bar {
  margin-bottom: 10px;
}

.search-bar input {
  display: flex;
  gap: 10px;
}

.search-bar button {
  padding: 5px 10px;
}

.custom-select {
  width: 150px; /* 원하는 크기로 조정 */
  height: 40px; /* 원하는 크기로 조정 */
  font-size: 16px; /* 원하는 글꼴 크기로 조정 */
}

.modal {
  display: flex;
  align-items: center;
  justify-content: center;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  z-index: 2;
}

.modal-content {
  background-color: #fff;
  width: 40%; /* 모달 창의 너비 설정 */
  max-width: 500px; /* 모달 창의 최대 너비 설정 */
  padding: 20px;
  border-radius: 5px;
}

</style>

