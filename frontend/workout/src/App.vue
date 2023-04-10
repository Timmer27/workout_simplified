<template>
  <div>
    <header  style="display: flex;">
      <div class="headerBox"></div>
      <div class="headerBox">
        <img alt="Vue logo" src="./assets/logo.png" id='header_logo'>
      </div>
      <div class="headerBox">
        <div>
          <img alt="Vue logo" src="./assets/logo.png" id='pic_icon'>
        </div>
        <div>
          사진 몰아보기
        </div>
      </div>
    </header>
    <main style="display: flex;">
        <div>
          <p>
            오늘의 인증샷
          </p>

          <!-- 오늘 운동 사진 출력 -->
          <div v-for="name in names" :key="name">
            <div>
              {{name}}
            </div>
            <div class="today_workout_pics">
              <!-- <source media="(min-width:650px)" srcset="./assets/logo.png"> -->
              <source media="all and (min-width: 768px)" srcset="./assets/logo.png">
              <img src="./assets/logo.png" alt="logo" class="today_workout_pics">
            </div>
          </div>
        </div>



          <!-- 운동 사진 등록 -->
          <nav id="uploadBox">
            <div class="uploadForm">
              <span>누구세요: </span>
              <select name="ppl_names" id="ppl_names">
                <option value="" selected disabled>본인 이름 고르셈</option>
                <option value="조성수">조성수</option>
                <option value="이재빈">이재빈</option>
                <option value="이종호">이종호</option>
              </select>
            </div>

            <div class="uploadForm">
              <span>오늘 인증할 날짜: </span>
              <span style="">
                {{getNewDate()}}
              </span>
              <!-- <input type="date" name="curr_date" id="curr_date" disabled> -->
            </div>

            <div class="uploadForm">
              <span>오늘 운동 사진 인증 ㄱㄱ</span>
              <input type="file" name="workout_file" id="workout_file" accept="image/*">
            </div>

            <div class="uploadForm">
              <div>
                다 올렸으면 저장 ㄱㄱ
              </div>
              <button>저장하기</button>
            </div>
          </nav>
        <div>

        </div>
    </main>
    <footer style="margin-top: 20px;">
      <div style="display: flex; place-content: space-evenly;">
        <div>
          <strong>이번 달 멸치</strong>
          <div>
            한 달 운동 제일 적게간 사람임
          </div>
          <div>
            <img alt="Vue logo" src="./assets/logo.png">
          </div>

          <div>
            이름: 이종호
          </div>
        </div>

        <table style="height: fit-content;">
          <tr>
            <th>이름</th>
            <th>한달 간 헬스장 방문 횟수</th>
          </tr>
          <tr v-for="(name, i) in names" :key="i">
            <td>
              {{ name }}
            </td>
            <td>
              {{ workoutCnt[i] }}
            </td>
          </tr>
        </table>
      </div>
      <!-- 아래 멸치사진 ㄱ -->
    </footer>
    
    <!-- {{curr_date}} -->
  </div>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'App',
  data() {
    return {
      names :['조성수' ,'이재빈', '이종호'],
      workoutCnt: [3,6,10],
      nowDate: function(){
        return "test"
      }
      // nowDate: getNewDate()
    }
  },
  components: {
    // HelloWorld
  },
  methods: {
    
    testMethod(){
      console.log('test')
    },

    getNewDate(){
      let myDate = new Date();
      let yy = String(myDate.getFullYear())  
      let mm = myDate.getMonth() + 1
      let mmm = (mm.toString().length < 2) ? '0' + mm : mm
      let dd = String(myDate.getDate() < 10 ? '0' + myDate.getDate() : myDate.getDate())
      let ddd = (dd.toString().length < 2) ? '0' + dd : dd
      let curr_date = yy + '-' + mmm + '-' + ddd
      return curr_date
    }
  },
}
</script>

<style>
@import "./assets/css/main.css";

</style>
