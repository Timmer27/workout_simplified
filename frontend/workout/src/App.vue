<template>
  <div>
    <header  style="display: flex;" class="border_divBox">
      <div class="headerBox"></div>
      <div class="headerBox border_divBox" style="display: flex; flex-flow: column; align-items: center;">
        <img alt="Vue logo" src="./assets/images/workout.png" id='header_logo'>
        <strong>
          운동체크 간단 웹앱
        </strong>
      </div>
      <div class="headerBox">
        <div>
          <img alt="Vue logo" src="./assets/images/book.png" id='pic_icon'>
        </div>
        <div>
          사진 몰아보기
        </div>
      </div>
    </header>
    <main style="display: flex; place-content: center;">
        <div>
          <p style="font-size: 18px; font-weight: bold;">
            오늘 운동한 사람 인증샷
          </p>

          <!-- 오늘 운동 사진 출력 -->
          <div v-for="(image, index) in workout_images" :key="index" class="">
            <div>
              {{workout_ppl[index]}}
            </div>
            <div class="today_workout_pics border_divBox">
              <!-- <source media="(min-width:650px)" srcset="./assets/logo.png"> -->
              <source media="all and (min-width: 768px)" srcset="./assets/logo.png">
              <img :src=image alt="logo" class="today_workout_pics">
            </div>
          </div>

          <!-- 운동 사진 등록 -->
          <nav id="uploadBox" class="border_divBox" style="margin-top: 20px;">
            <p style="font-size: 18px; font-weight: bold;">
              운동한거 인증하셈 ㄱㄱ
            </p>
            <div class="uploadForm">
              <span>누구세요: </span>
              <select name="ppl_names" id="ppl_names" ref="ppl_names" @change="selectedValue">
                <option value="0" selected disabled>본인 이름 고르셈</option>
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
              <div>
                <span>오늘 운동 사진 파일로 인증 ㄱㄱ</span>
              </div>
              <div>
                <form @submit.prevent="uploadFile" enctype="multipart/form-data">
                  <input @change="handleFileUpload" ref="file" type="file" name="workout_file" id="workout_file" accept="image/*">
                  <div class="uploadForm">
                    <div>
                      다 올렸으면 저장 ㄱㄱ
                    </div>
                    <button type="submit">저장하기</button>
                  </div>
                </form>
                <!-- enctype="multipart/form-data" -->
              </div>
            </div>
          </nav>
          
        </div>
    </main>
    <footer style="margin-top: 20px;">
      <div style="display: flex; place-content: space-evenly;">
        <div class="border_divBox">
          <strong>이번 달 멸치</strong>
          <div>
            한 달 운동 제일 적게간 사람
          </div>
          <div class="border_divBox">
            <img alt="Vue logo" style="width:150px; height:120px;" :src=name_lowest_pic>
          </div>

          <div style="min-width: 6em;">
            이름: {{name_lowest}}
          </div>
        </div>

        <table style="height: fit-content;">
          <tr>
            <th style="width: 6em;">이름</th>
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
    </footer>
    <div @mouseleave="isVisible=false">
      <greetings :status="vueString" :isVisible="isVisible"/>
    </div>
    
    
    
    
    <div>
      <button @click="location.reload();">testButton</button>
    </div>
  </div>
</template>

<script>
import greetings from './components/modalPopup.vue';
import axios from 'axios';

const path = "http://127.0.0.1:5000";

export default {
  name: 'App',
  data() {
    return {
      names : [],
      workoutCnt: [],
      
      workout_ppl: [],
      workout_images: [],
      
      name_lowest: '',
      name_lowest_pic: '',

      selectedFile: null,
      selected_name: '',

      isVisible: false,
      vueString: "",

    }
  },

  setup(){
  },

  // DOM 세팅
  mounted(){
    axios.get(path + '/')
      .then(res => {
        for(var i = 0; i < res.data['result_cnt'].length; i+=1){
          this.names.push(res.data['result_cnt'][i][0])
          this.workoutCnt.push(res.data['result_cnt'][i][1])
        }
        
        for(var j = 0; j < Object.values(res.data['result_todayPic']).length; j+=1){
          this.workout_ppl.push(res.data['result_todayPic'][j][0])
          this.workout_images.push(require("./assets/images/" + res.data['result_todayPic'][j][1]))
        }
        
        this.name_lowest =  this.names[this.names.length-1]
        this.name_lowest_pic = require("./assets/images/" + this.names[this.names.length-1] + '.png')
      });
  },
  components: {
    greetings
  },
  methods: {

    selectedValue(){
      this.selected_name = this.$refs.ppl_names.value
      // console.log(this.selected_name)
    },

    handleFileUpload(){
      this.selectedFile = this.$refs.file.files[0];
      // console.log(this.selectedFile);
    },
    
    // 파일 업로드
    uploadFile(){
      // 파일 없거나 이름 선택 안됬을 때
      if (this.selectedFile == null){
        this.vueString = '파일 첨부하고 저장 ㄱㄱ'
        this.isVisible = true        
        return null;
      }
      else if(this.selected_name == ''){
        this.vueString = '본인 이름 선택 먼저 ㄱㄱ'
        this.isVisible = true    
        return null;
      }
      else{
        const headers = { 'Content-Type': 'multipart/form-data' };
        let formData = new FormData();
        formData.append("file", this.selectedFile);
        formData.append('name', this.selected_name);
        
        // 여기섯 backend로 넘기기
        axios.post(path + "/uploadFile", formData, {headers}).then(res => {
          if(res.data == -1){
            this.vueString = '하루 2번 인증 ㄴㄴ'
            this.isVisible = true        
            return null;
          }
          else if (res.data == 1){
            return null
            // window.location.reload(true);
          }
        }).catch(err =>{
          console.log(err + ': 에러 발생!')
        });
      }
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
