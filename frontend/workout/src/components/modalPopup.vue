<template>
    <div v-show="isVisible" class="outer">
      <div class="inner">
        <h2 style="color: red;">{{status}}</h2>
        <p>
          닫으려면 창 바깥쪽 클릭 ㄱ
        </p>
      </div>
    </div>
</template>
  
<script>
  export default {
    name: 'modalPopup',
    props:{
        status: String,
        isVisible: Boolean,
    },

    data() {
        return {
          // isVisible: false,
        }
    },
    methods:{
      // closePopup(){
      //   this.isVisible = false
      // }
    }
  };
</script>
  
<style scoped> /* 이 파일에만 적용되는 스타일 */
.outer {
  position: relative;
  width: 100%;
  height: 100%;
  margin:0;
}

.inner {
  position: fixed;
  transform: translate(-50%,-50%);
  left: 50%;
  top: 50%;
  min-width: 20rem;
  min-height: 8rem;
  border: 2px solid;
  background: beige;
}
</style>