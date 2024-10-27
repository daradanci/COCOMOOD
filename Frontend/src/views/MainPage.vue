<template v-if="isAuthenticated">
  <div class="superframe-container10">
    <div class="superframe-superframe">
      <div class="superframe-body">
        <div class="superframe-header">
          <div class="superframe-container11">
            <button class="superframe-buttonmargin">
              <div class="superframe-component2">
                <span
                  class="superframe-text10 www.livelib.ruSourceSansProSemiBold18"
                >
                  <!-- <span>Выйти</span> -->
                  <router-link to="/" class="exit-btn">Выйти</router-link>
                </span>
              </div>
            </button>

            <span
              class="superframe-text12 www.livelib.ruSourceSansProSemiBold18"
            >
              <span>ЧИТАЙ И СЧИТАЙ!</span>
            </span>
            <img
              alt="logo4820"
              src="/external/logo4820-1gif-200h.png"
              class="superframe-logo"
            />
          </div>
        </div>
        <div class="superframe-main">
          <div class="superframe-margin10"></div>
          <div class="superframe-margin11">
            <div class="superframe-container12">
              <div class="superframe-component1">
                <donut-chart />

                <span class="superframe-text14 www.livelib.ruInterBold85">
                  <span>10</span>
                </span>
                <span class="superframe-text16 www.livelib.ruInterRegular36">
                  <span>книг</span>
                </span>
              </div>
              <div class="superframe-margin12">
                <div class="superframe-container13">
                  <div class="superframe-container14">
                    <span class="superframe-text18">
                      <span>Ты в трекере с</span>
                    </span>
                    <div class="superframe-container15">
                      <span class="superframe-text20">
                        <span>27.10.2024</span>
                      </span>
                    </div>
                  </div>
                </div>
              </div>
              <!-- <div class="superframe-listmargin1">
                <div class="superframe-list1">
                  <div class="superframe-itemmargin1">
                    <div class="superframe-item1">
                      <div class="superframe-paragraph1">
                        <span
                          class="superframe-text22 www.livelib.ruSemanticItem2"
                        >
                          8
                        </span>
                        <span
                          class="superframe-text23 www.livelib.ruSemanticItem"
                        >
                          <span>/ 10</span>
                        </span>
                      </div>
                      <div class="superframe-container16">
                        <span
                          class="superframe-text25 www.livelib.ruSemanticItem"
                        >
                          <span>Осталось</span>
                        </span>
                      </div>
                    </div>
                  </div>
                  <div class="superframe-itemmargin2">
                    <div class="superframe-item2">
                      <div class="superframe-paragraph2">
                        <span
                          class="superframe-text27 www.livelib.ruSemanticItem2"
                        >
                        </span>
                        <span
                          class="superframe-text28 www.livelib.ruSemanticItem"
                        >
                        </span>
                      </div>
                      <div class="superframe-container17">
                        <span
                          class="superframe-text30 www.livelib.ruSemanticItem"
                        >
                        </span>
                      </div>
                    </div>
                  </div>
                  <div class="superframe-itemmargin3">
                    <div class="superframe-item3">
                      <div class="superframe-container18">
                        <span
                          class="superframe-text32 www.livelib.ruSemanticItem2"
                        >
                        </span>
                      </div>
                      <div class="superframe-container19">
                        <span
                          class="superframe-text33 www.livelib.ruSemanticItem"
                        >
                        </span>
                      </div>
                    </div>
                  </div>
                </div>
              </div> -->
            </div>
          </div>

          <div class="superframe-articlemargin">
            <div class="superframe-article">
              <div class="superframe-heading2">
                <span class="superframe-text35 www.livelib.ruSemanticHeading2">
                  <span>Прочитанные книги – 2 из 10</span>
                </span>
              </div>

              <book-list></book-list>
            </div>
          </div>
          <div class="superframe-margin20">
            <div class="superframe-overlay2">
              <div class="superframe-margin21">
                <div class="superframe-container31">
                  <span class="superframe-text73">
                    <span class="superframe-text74">
                      Твоя
                      <span v-html="raw1a25"></span>
                    </span>
                    <span class="superframe-text75"> заинтересованность </span>
                    <span>в среднем составляет:</span>
                  </span>
                  <span
                    class="superframe-text77 www.livelib.ruSemanticItem2 Text"
                  >
                    <span>50%</span>
                  </span>
                </div>
              </div>
            </div>
          </div>
          <div class="superframe-margin15">
            <div class="superframe-overlay1">
              <div class="superframe-margin16">
                <div class="superframe-container24">
                  <span class="superframe-text57">
                    <span class="superframe-text58">
                      Твое среднее
                      <span v-html="rawj5ir"></span>
                    </span>
                    <span class="superframe-text59">время чтения </span>
                    <span>в среднем составляет:</span>
                  </span>
                  <span class="superframe-text61 Text">
                    <span>1 мин</span>
                  </span>
                </div>
              </div>
            </div>
          </div>

          <div class="superframe-margin15-1">
            <div class="superframe-overlay1">
              <div class="superframe-margin16">
                <div class="superframe-container24">
                  <span class="superframe-text57">
                    <span class="superframe-text58">
                      За последнюю
                      <span v-html="rawj5ir"></span>
                    </span>
                    <span class="superframe-text59">неделю </span>
                    <span>ты притрагивался к книгам: </span>
                  </span>
                  <span class="superframe-text61 Text">
                    <span>1</span>

                    <span
                      class="superframe-text57"
                      style="color: aliceblue; font-size: 26px"
                      >/7 дней</span
                    >
                  </span>
                </div>
              </div>
            </div>
          </div>

          <div class="superframe-margin15-2">
            <div class="superframe-overlay1">
              <div class="superframe-margin16">
                <div class="superframe-container24">
                  <span class="superframe-text57">
                    <span class="superframe-text59">Осталось: </span>
                    <span class="superframe-text61 Text">
                      <span>8</span>
                    </span>
                    <span>/10 книг и </span>
                    <span class="superframe-text61 Text">
                      <span>364</span>
                    </span>
                    <span>/365 дней</span>
                  </span>
                </div>
              </div>
            </div>
          </div>

          <div class="superframe-container25">
            <div class="superframe-container26">
              <div class="superframe-margin17">
                <div class="superframe-container27">
                  <div class="superframe-margin18">
                    <span class="superframe-text63">
                      <span class="superframe-text64">
                        Попробуй нашего
                        <span v-html="rawrl3p"></span>
                      </span>
                      <span class="superframe-text65">
                        Телеграм-бота
                        <span v-html="rawdoc1"></span>
                      </span>
                    </span>
                  </div>
                </div>
              </div>
              <a
                href="https://www.livelib.ru/challenge/2024"
                target="_blank"
                rel="noreferrer noopener"
                class="superframe-link5"
              >
                <div class="superframe-link6">
                  <div class="superframe-container28">
                    <span class="superframe-text66">
                      <span class="www.livelib.ruSemanticLink6">
                        Книжный трекер
                      </span>
                      <br />
                      <br />
                    </span>
                  </div>
                  <div class="superframe-container29">
                    <span class="superframe-text70">
                      &quot;Люди перестают мыслить, когда перестают читать&quot;
                    </span>
                    <div class="superframe-object">
                      <span class="superframe-text71">
                        <span>
                          Дени Дидро
                          <span v-html="raw6vvw"></span>
                        </span>
                      </span>
                    </div>
                  </div>
                </div>
              </a>
              <div class="superframe-margin19">
                <div class="superframe-container30">
                  <div class="superframe-filled-black">
                    <a href="https://t.me/CocoMoodBot" target="”_blank”">
                      <div class="superframe-artboard">
                        <img
                          alt="Path4520"
                          src="/external/path4520-8xx.svg"
                          class="superframe-path"
                        />
                      </div>
                    </a>
                  </div>

                  <div class="superframe-component42" @click="showAlert">
                    <div class="superframe-image4">
                      <img
                        alt="SVGsprite18svgfillI361"
                        src="/external/svgsprite18svgfilli361-nx1n.svg"
                        class="superframe-sv-gsprite18svgfill2"
                      />
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="superframe-spv"></div>
      </div>
    </div>
  </div>
</template>

<script>
import BookList from '../components/BookList.vue'
import DonutChart from '../components/DonutChart.vue'
import { useMainStore } from '@/stores/store'
export default {
  components: { DonutChart, BookList },
  name: 'superframe',
  data() {
    return {
      rawj5ir: ' ',
      rawrl3p: ' ',
      rawdoc1: ' ',
      raw6vvw: ' ',
      raw1a25: ' ',
      books: [
        {
          id: 1,
          title: 'Магистр дьявольского культа. Том 1',
          author: 'Мосян Тунсю',
          rating: '4.8',
          image: '/path/to/image1.jpg',
          link: 'https://www.livelib.ru/book/1003989922-magistr-dyavolskogo-kulta-tom-1-mosyan-tunsyu',
        },
        {
          id: 2,
          title: 'Замминистр',
          author: 'Тунсю Монсян',
          rating: '4.7',
          image: '/path/to/image2.jpg',
          link: 'https://www.livelib.ru/book/1004160469-magistr-dyavolskogo-kulta-tom-4-mosyan-tunsyu',
        },
      ],
    }
  },
  metaInfo: {
    title: 'exported project',
  },
  setup() {
    const mainStore = useMainStore()
    const isAuthenticated = mainStore.isAuthenticated // для геттера
    return {
      isAuthenticated,
      mainStore,
    }
  },
  methods: {
    showAlert() {
      window.alert(
        'Книжный трекер от команды COCOMOOD поможет тебе выработать привычку регулярного чтения. Ты сам ставишь себе цель, а мы поможем её достичь при помощи напоминаний и рекомендаций ;)',
      )
    },
  },
}
</script>

<style scoped>
.superframe-container10 {
  width: 100%;
  display: flex;
  overflow: auto;
  min-height: 100vh;
  align-items: center;
  flex-direction: column;
}
.superframe-superframe {
  width: 100%;
  height: auto;
  display: flex;
  padding: 0 0 16px;
  align-items: center;
  flex-shrink: 0;
  flex-direction: column;
  background-color: #2d3133;
}
.superframe-body {
  width: 1920px;
  height: 1626px;
  display: flex;
  position: relative;
  align-items: center;
  flex-shrink: 0;
  flex-direction: column;
  background-color: var(--dl-color-www.livelib.ru-black);
}
.superframe-header {
  display: flex;
  padding: 0 390px;
  align-self: stretch;
  align-items: center;
  flex-direction: column;
  background-color: #2d3133;
}
.superframe-container11 {
  width: 1140px;
  height: 72px;
  display: flex;
  position: relative;
  align-items: flex-start;
  flex-shrink: 0;
  background-color: #16171726;
}
.superframe-buttonmargin {
  top: 16px;
  left: 1006.5900268554688px;
  /* width: 133px; */
  /* height: 40px; */
  display: flex;
  /* padding: 0 0 0 16px; */
  position: absolute;
  align-items: flex-start;
  flex-shrink: 0;
  flex-direction: column;
  background-color: #2d3133;
  border: #2d3133;
}
.superframe-component2 {
  width: 117.41000366210938px;
  height: 40px;
  display: flex;
  padding: 7.5px 33.7599983215332px 8.5px 33.77000045776367px;
  align-items: center;
  flex-shrink: 0;
  border-radius: 20px;
  justify-content: center;
  background-color: rgba(10, 163, 136, 1);
}
.superframe-text10 {
  color: #2d3133;
  height: auto;
  text-align: center;
  line-height: 24px;
}
.superframe-text12 {
  top: 23px;
  left: 195px;
  color: #ffffff;
  width: 731px;
  height: auto;
  position: absolute;
  text-align: center;
  line-height: 24px;
}
.superframe-logo {
  top: 8px;
  left: 0px;
  width: 200px;
  height: 56px;
  position: absolute;
}
.superframe-main {
  width: 1140px;
  height: 1498px;
  display: flex;
  z-index: 1;
  position: relative;
  align-items: flex-start;
  flex-shrink: 0;
  justify-content: center;
  background-color: #2d3133;
}
.superframe-margin10 {
  top: 96px;
  left: 0px;
  width: 1140px;
  border: 2px dashed rgba(120, 120, 120, 0.4);
  height: 71px;
  display: flex;
  padding: 32px 0 0;
  position: absolute;
  align-items: center;
  flex-shrink: 0;
  flex-direction: column;
  justify-content: center;
}
.superframe-margin11 {
  top: 220px;
  right: -6px;
  width: 1140px;
  height: 388px;
  display: flex;
  padding: 10px 0 30px 388px;
  position: absolute;
  align-items: flex-start;
  flex-shrink: 0;
  flex-direction: column;
}
.superframe-container12 {
  top: -39px;
  left: 0px;
  width: 1159px;
  height: 492px;
  display: flex;
  position: absolute;
  align-self: stretch;
  align-items: flex-start;
  flex-direction: column;
  padding-bottom: 387px;
}
.superframe-component1 {
  width: 288px;
  height: 288px;
  display: flex;
  position: relative;
  align-items: flex-start;
  flex-shrink: 0;
  background-color: aqua;
}
.superframe-vector1 {
  top: 10px;
  left: 10px;
  width: 268px;
  height: 268px;
  opacity: 0.17;
  position: absolute;
}
.superframe-vector2 {
  top: 32px;
  left: 32px;
  width: 224px;
  height: 224px;
  opacity: 0.23;
  position: absolute;
}
.superframe-vector3 {
  top: 54px;
  left: 54px;
  width: 180px;
  height: 180px;
  opacity: 0.23;
  position: absolute;
}
.superframe-vector4 {
  top: 10px;
  left: 10px;
  width: 268px;
  height: 268px;
  position: absolute;
}
.superframe-vector5 {
  top: 32px;
  left: 32px;
  width: 224px;
  height: 224px;
  position: absolute;
}
.superframe-vector6 {
  top: 54px;
  left: 54px;
  width: 180px;
  height: 180px;
  position: absolute;
}
.superframe-text14 {
  top: 71px;
  left: 93.5px;
  color: #2d3133;
  height: auto;
  position: absolute;
  text-align: center;
  line-height: normal;
  margin-top: 134px;
  margin-left: 16px;
  font-size: 26px;
}
.superframe-text16 {
  top: 151px;
  left: 104px;
  color: #2d3133;
  height: auto;
  position: absolute;
  text-align: left;
  line-height: normal;
  margin-top: 70px;
  margin-left: 35px;
  font-size: 20px;
}
.superframe-margin12 {
  top: -4px;
  left: 163px;
  width: 290px;
  display: flex;
  padding: 8px 0 56px 16px;
  z-index: 1;
  position: absolute;
  align-self: stretch;
  align-items: flex-start;
  flex-direction: column;
}
.superframe-container13 {
  width: 736px;
  height: 48px;
  display: flex;
  position: relative;
  align-self: stretch;
  align-items: flex-start;
}
.superframe-container14 {
  top: 2px;
  left: 93px;
  width: 130px;
  display: flex;
  position: absolute;
  align-items: flex-start;
  flex-shrink: 0;
  flex-direction: column;
}
.superframe-text18 {
  color: #ffffff;
  height: auto;
  text-align: left;
  line-height: 22px;
  font-size: 16px;
  padding: -2px;
  margin-left: 20px;
}
.superframe-container15 {
  display: flex;
  align-self: stretch;
  align-items: flex-start;
  flex-direction: column;
}
.superframe-text20 {
  color: #ffffff;
  height: auto;
  text-align: left;
  line-height: 22px;
  margin-left: 30px;
  font-size: 20px;
}
.superframe-listmargin1 {
  display: flex;
  padding: 0 0 0 16px;
  z-index: 2;
  position: relative;
  align-self: stretch;
  align-items: flex-start;
  flex-direction: column;
  margin-right: 20px;
}
.superframe-list1 {
  top: 0px;
  right: 0px;
  width: 743px;
  display: flex;
  position: absolute;
  align-self: stretch;
  align-items: flex-start;
  flex-shrink: 0;
}
.superframe-itemmargin1 {
  height: 112px;
  display: flex;
  padding: 0 0 16px;
  align-self: stretch;
  align-items: flex-start;
  flex-shrink: 0;
  flex-direction: column;
  justify-content: center;
}
.superframe-item1 {
  width: 194px;
  height: 96px;
  display: flex;
  align-items: flex-start;
  flex-shrink: 0;
  flex-direction: column;
}
.superframe-paragraph1 {
  width: 194px;
  height: 56px;
  display: flex;
  position: relative;
  align-self: stretch;
  align-items: flex-start;
}
.superframe-text22 {
  top: -0.5px;
  color: #ffffff;
  width: 34px;
  height: auto;
  position: absolute;
  text-align: left;
  line-height: 40px;
  font-size: 60px;
}
.superframe-text23 {
  top: 15.5px;
  left: 34.02000045776367px;
  color: #ffffff;
  width: 40px;
  height: auto;
  position: absolute;
  text-align: left;
  line-height: 40px;
  font-size: 20px;
}
.superframe-container16 {
  display: flex;
  align-self: stretch;
  align-items: flex-start;
  flex-direction: column;
}
.superframe-text25 {
  color: #ffffff;
  height: auto;
  align-self: stretch;
  text-align: left;
  line-height: 40px;
}
.superframe-itemmargin2 {
  height: 112px;
  display: flex;
  padding: 0 0 16px;
  align-self: stretch;
  align-items: flex-start;
  flex-shrink: 0;
  flex-direction: column;
  justify-content: center;
}
.superframe-item2 {
  width: 194px;
  height: 96px;
  display: flex;
  align-items: flex-start;
  flex-shrink: 0;
  flex-direction: column;
}
.superframe-paragraph2 {
  width: 194px;
  height: 56px;
  display: flex;
  position: relative;
  align-self: stretch;
  align-items: flex-start;
}
.superframe-text27 {
  top: -0.5px;
  color: #ffffff;
  width: 34px;
  height: auto;
  position: absolute;
  text-align: left;
  line-height: 40px;
  font-size: 60px;
}
.superframe-text28 {
  top: 15.5px;
  left: 34.02000045776367px;
  color: #ffffff;
  width: 40px;
  height: auto;
  position: absolute;
  text-align: left;
  line-height: 40px;
  font-size: 20px;
}
.superframe-container17 {
  display: flex;
  align-self: stretch;
  align-items: flex-start;
  flex-direction: column;
}
.superframe-text30 {
  color: #ffffff;
  height: auto;
  align-self: stretch;
  text-align: left;
  line-height: 40px;
}
.superframe-itemmargin3 {
  height: 112px;
  display: flex;
  padding: 0 0 16px;
  align-self: stretch;
  align-items: flex-start;
  flex-shrink: 0;
  flex-direction: column;
  justify-content: center;
}
.superframe-item3 {
  width: 194px;
  height: 96px;
  display: flex;
  align-items: flex-start;
  flex-shrink: 0;
  flex-direction: column;
}
.superframe-container18 {
  display: flex;
  padding: 0 0 16.5px;
  align-self: stretch;
  align-items: flex-start;
  flex-direction: column;
}
.superframe-text32 {
  color: #ffffff;
  height: auto;
  align-self: stretch;
  text-align: left;
  line-height: 40px;
  font-size: 60px;
}
.superframe-container19 {
  display: flex;
  align-self: stretch;
  align-items: flex-start;
  flex-direction: column;
}
.superframe-text33 {
  color: #ffffff;
  height: auto;
  align-self: stretch;
  text-align: left;
  line-height: 40px;
}
.superframe-articlemargin {
  top: 569px;
  right: -9px;
  width: 1140px;
  display: flex;
  padding: 32px 0 24px;
  position: absolute;
  align-items: flex-start;
  flex-shrink: 0;
  flex-direction: column;
}
.superframe-article {
  gap: 24px;
  display: flex;
  align-self: stretch;
  align-items: flex-start;
  flex-direction: column;
}
.superframe-heading2 {
  display: flex;
  align-self: stretch;
  align-items: flex-start;
  flex-direction: column;
}
.superframe-text35 {
  margin-top: 20px;
  align-self: center;
  color: #ffffff;
  height: auto;
  /* align-self: stretch; */
  text-align: left;
  line-height: 40px;
  font-size: 40px;
}
.superframe-background {
  height: 559px;
  display: flex;
  padding: 4px 0 46px;
  align-self: stretch;
  align-items: center;
  flex-shrink: 0;
  border-radius: 24px;
  flex-direction: column;
  background-color: #2d3133;
}
.superframe-listmargin2 {
  height: 451px;
  display: flex;
  padding: 0 0 36px;
  align-self: stretch;
  align-items: flex-start;
  flex-shrink: 0;
  flex-direction: column;
}
.superframe-list2 {
  display: flex;
  padding: 0 182px;
  flex-wrap: wrap;
  align-self: stretch;
  align-items: flex-start;
  flex-shrink: 0;
  justify-content: center;
}
.superframe-itemmargin4 {
  width: 194px;
  height: 480px;
  display: flex;
  /* padding: 56px 12px 0; */
  align-items: flex-start;
  flex-shrink: 0;
  flex-direction: column;
}
.superframe-item4 {
  gap: -8px;
  width: 170px;
  height: 375px;
  display: flex;
  align-items: flex-start;
  flex-shrink: 0;
  border-radius: 8px 8px 24px 24px;
  flex-direction: column;
  background-color: #2d3133;
}
.superframe-link1 {
  display: contents;
}
.superframe-link2 {
  width: 170px;
  height: 256px;
  display: flex;
  overflow: hidden;
  align-items: center;
  flex-shrink: 0;
  border-radius: 8px;
  background-color: #2d3133;
}
.superframe-mosyan-tunsyu-magistrdyavolskogokulta-tom1jpg {
  width: 170px;
  height: 256px;
  display: flex;
  overflow: hidden;
  position: relative;
  align-items: flex-start;
  flex-shrink: 0;
  background-size: cover;
  background-image: url('/external/tq_p8-bzauu2y-8xma-200w.png');
}
.superframe-margin13 {
  height: 118px;
  display: flex;
  align-self: stretch;
  align-items: flex-start;
  flex-shrink: 0;
  flex-direction: column;
}
.superframe-background-border1 {
  width: 170px;
  height: 118px;
  display: flex;
  position: relative;
  align-self: stretch;
  align-items: flex-start;
  border-color: rgba(227, 229, 230, 1);
  border-style: solid;
  border-width: 0 1px 1px;
  border-radius: 0 0 24px 24px;
  background-color: #2d3133;
}
.superframe-component61 {
  top: 18px;
  left: 16px;
  width: 138px;
  height: 320px;
  display: flex;
  overflow: hidden;
  position: absolute;
  align-items: flex-start;
  flex-shrink: 0;
}
.superframe-text37 {
  color: var(--dl-color-www.livelib.ru-shark);
  width: 114px;
  height: auto;
  position: absolute;
  text-align: left;
  line-height: 16px;
}
.superframe-linkmargin1 {
  top: 50px;
  left: 16px;
  width: 138px;
  height: 33px;
  display: flex;
  padding: 9px 0 7px;
  position: absolute;
  align-items: flex-start;
  flex-shrink: 0;
  flex-direction: column;
}
.superframe-component31 {
  display: flex;
  overflow: hidden;
  align-self: stretch;
  align-items: flex-start;
  flex-direction: column;
}
.superframe-text43 {
  color: var(--dl-color-www.livelib.ru-shark);
  height: auto;
  align-self: stretch;
  text-align: left;
  line-height: 17px;
}
.superframe-component81 {
  top: 16px;
  left: 138px;
  width: 32px;
  height: 26px;
  display: flex;
  position: absolute;
  align-items: flex-start;
  flex-shrink: 0;
}
.superframe-background-shadow1 {
  top: 12px;
  left: 18px;
  width: 3px;
  height: 3px;
  position: absolute;
  border-radius: 1.5px;
}
.superframe-container20 {
  top: 83px;
  left: 16px;
  width: 138px;
  display: flex;
  padding: 0 0 11px 28px;
  position: absolute;
  align-items: center;
  flex-shrink: 0;
}
.superframe-container21 {
  display: flex;
  align-items: flex-start;
  flex-direction: column;
}
.superframe-text45 {
  color: var(--dl-color-www.livelib.ru-shark);
  height: auto;
  text-align: left;
  line-height: 24px;
}
.superframe-image1 {
  width: 24px;
  height: 24px;
  display: flex;
  z-index: 1;
  align-items: flex-start;
  flex-shrink: 0;
  flex-direction: column;
}
.superframe-sv-gsprite13svgfill1 {
  width: 24px;
  height: 24px;
}
.superframe-itemmargin5 {
  width: 194px;
  height: 422px;
  display: flex;
  /* padding: 56px 12px 0; */
  align-items: flex-start;
  flex-shrink: 0;
  flex-direction: column;
}
.exit-btn {
  color: #ffffff;
}
.superframe-item5 {
  gap: -8px;
  width: 170px;
  height: 366px;
  display: flex;
  align-items: flex-start;
  flex-shrink: 0;
  border-radius: 8px 8px 24px 24px;
  flex-direction: column;
  background-color: #2d3133;
}
.superframe-link3 {
  display: contents;
}
.superframe-link4 {
  width: 170px;
  height: 256px;
  display: flex;
  overflow: hidden;
  align-items: center;
  flex-shrink: 0;
  border-radius: 8px;
  background-color: #2d3133;
}
.superframe-mosyan-tunsyu-magistrdyavolskogokulta-tom4jpg {
  width: 170px;
  height: 256px;
  display: flex;
  overflow: hidden;
  position: relative;
  align-items: flex-start;
  flex-shrink: 0;
  background-size: cover;
  background-image: url('/external/tq_3jmry409h--og1p-200w.png');
}
.superframe-margin14 {
  height: 118px;
  display: flex;
  align-self: stretch;
  align-items: flex-start;
  flex-shrink: 0;
  flex-direction: column;
}
.superframe-background-border2 {
  width: 170px;
  height: 118px;
  display: flex;
  position: relative;
  align-self: stretch;
  align-items: flex-start;
  border-color: rgba(227, 229, 230, 1);
  border-style: solid;
  border-width: 0 1px 1px;
  border-radius: 0 0 24px 24px;
  background-color: #2d3133;
}
.superframe-component62 {
  top: 18px;
  left: 16px;
  width: 138px;
  height: 32px;
  display: flex;
  overflow: hidden;
  position: absolute;
  align-items: flex-start;
  flex-shrink: 0;
}
.superframe-text47 {
  color: var(--dl-color-www.livelib.ru-shark);
  width: 114px;
  height: auto;
  position: absolute;
  text-align: left;
  line-height: 16px;
}
.superframe-linkmargin2 {
  top: 50px;
  left: 16px;
  width: 138px;
  height: 33px;
  display: flex;
  padding: 9px 0 7px;
  position: absolute;
  align-items: flex-start;
  flex-shrink: 0;
  flex-direction: column;
}
.superframe-component32 {
  display: flex;
  overflow: hidden;
  align-self: stretch;
  align-items: flex-start;
  flex-direction: column;
}
.superframe-text53 {
  color: var(--dl-color-www.livelib.ru-shark);
  height: auto;
  align-self: stretch;
  text-align: left;
  line-height: 17px;
}
.superframe-component82 {
  top: 16px;
  left: 138px;
  width: 32px;
  height: 26px;
  display: flex;
  position: absolute;
  align-items: flex-start;
  flex-shrink: 0;
}
.superframe-background-shadow2 {
  top: 12px;
  left: 18px;
  width: 3px;
  height: 3px;
  position: absolute;
  border-radius: 1.5px;
}
.superframe-container22 {
  top: 83px;
  left: 16px;
  width: 138px;
  display: flex;
  padding: 0 0 11px 28px;
  position: absolute;
  align-items: center;
  flex-shrink: 0;
}
.superframe-container23 {
  display: flex;
  align-items: flex-start;
  flex-direction: column;
}
.superframe-text55 {
  color: var(--dl-color-www.livelib.ru-shark);
  height: auto;
  text-align: left;
  line-height: 24px;
}
.superframe-image2 {
  width: 24px;
  height: 24px;
  display: flex;
  z-index: 1;
  align-items: flex-start;
  flex-shrink: 0;
  flex-direction: column;
}
.superframe-sv-gsprite13svgfill2 {
  width: 24px;
  height: 24px;
}
.superframe-margin15 {
  top: 676px;
  right: 4px;
  width: 752px;
  display: flex;
  padding: 0 0 39px;
  position: absolute;
  align-items: flex-end;
  flex-shrink: 0;
  flex-direction: column;
}
.superframe-margin15-1 {
  top: 740px;
  right: 4px;
  width: 752px;
  display: flex;
  padding: 0 0 39px;
  position: absolute;
  align-items: flex-end;
  flex-shrink: 0;
  flex-direction: column;
}
.superframe-margin15-2 {
  top: 900px;
  right: 4px;
  width: 752px;
  display: flex;
  padding: 0 0 39px;
  position: absolute;
  align-items: flex-end;
  flex-shrink: 0;
  flex-direction: column;
}
.superframe-overlay1 {
  top: -394px;
  left: -1px;
  width: 752px;
  height: 91px;
  display: flex;
  padding: 0 28px 28px 22px;
  position: absolute;
  align-items: flex-start;
  flex-shrink: 0;
  border-radius: 24px;
  flex-direction: column;
  background-color: #2d3133;
}
.superframe-margin16 {
  width: 606px;
  height: 88px;
  display: flex;
  padding: 2px 0 6px;
  align-items: flex-start;
  flex-shrink: 0;
  flex-direction: column;
}
.superframe-container24 {
  gap: -2.842170943040401e-14px;
  width: 711px;
  height: 50%;
  display: flex;
  position: relative;
  align-items: flex-start;
  flex-shrink: 0;
}
.superframe-text57 {
  color: #ffffff;
  width: 754px;
  height: auto;
  font-size: 26px;
  box-shadow: rgba(0, 0, 0, 0.25) 0px 4px 4px 0px;
  font-style: Light;
  text-align: left;
  font-family: Source Sans Pro;
  font-weight: 300;
  line-height: 32px;
  font-stretch: normal;
  text-decoration: none;
}
.superframe-text58 {
  font-weight: 300;
}
.superframe-text59 {
  font-weight: 600;
}
.superframe-text61 {
  color: rgba(10, 163, 136, 1);
  width: 145px;
  height: auto;
  text-align: left;
  line-height: 30px;
  font-size: 40px;
  margin-left: 20px;
}
.superframe-container25 {
  flex: 0 0 auto;
  width: 1140px;
  height: auto;
  display: flex;
  align-items: center;
  flex-direction: column;
}
.superframe-container26 {
  width: 1140px;
  height: 98px;
  display: flex;
  position: relative;
  align-self: stretch;
  align-items: flex-start;
}
.superframe-margin17 {
  top: 17px;
  left: 780px;
  width: 240px;
  height: 57px;
  display: flex;
  padding: 0 20px 0 0;
  position: absolute;
  align-items: flex-start;
  flex-shrink: 0;
  flex-direction: column;
}
.superframe-container27 {
  width: 240px;
  display: flex;
  align-items: flex-start;
  flex-shrink: 0;
  flex-direction: column;
}
.superframe-margin18 {
  width: 254px;
  height: 36px;
  display: flex;
  padding: 0 0 10px;
  align-self: flex-start;
  align-items: flex-start;
  flex-direction: column;
}
.superframe-text63 {
  height: auto;
  font-size: 16px;
  align-self: stretch;
  font-style: Regular;
  text-align: left;
  font-family: Source Sans Pro;
  font-weight: 400;
  line-height: 22px;
  font-stretch: normal;
  text-decoration: none;
}
.superframe-text64 {
  font-weight: 400;
  color: #ffffff;
}
.superframe-text65 {
  font-weight: 600;
  color: #ffffff;
}
.superframe-link5 {
  display: contents;
}
.superframe-link6 {
  top: 0px;
  left: 0px;
  width: 495px;
  height: 98px;
  display: flex;
  position: absolute;
  align-items: flex-start;
  flex-shrink: 0;
}
.superframe-container28 {
  right: 0px;
  width: 498px;
  bottom: 0px;
  height: 91px;
  display: flex;
  position: absolute;
  align-items: flex-start;
  flex-direction: column;
}
.superframe-text66 {
  color: #2d3133;
  height: auto;
  align-self: flex-start;
  text-align: left;
  line-height: 49px;
}
.superframe-container29 {
  gap: 5px;
  top: 98px;
  left: 0px;
  width: 499px;
  height: 74px;
  display: flex;
  padding: 12px 4px 15px;
  position: absolute;
  align-items: flex-start;
  flex-shrink: 0;
  flex-direction: column;
}
.superframe-text70 {
  color: #ffffff;
  height: auto;
  text-align: left;
  line-height: 24px;
}
.superframe-object {
  width: 138.22000122070312px;
  height: 18px;
  display: flex;
  overflow: hidden;
  position: relative;
  align-items: flex-start;
  flex-shrink: 0;
}
.superframe-text71 {
  top: -3px;
  color: rgb(red, rgb(0, 149, 0), blue);
  width: 91px;
  height: 20px;
  position: absolute;
  text-align: left;
  line-height: 24px;
}
.superframe-margin19 {
  top: 0px;
  left: 994px;
  width: 146px;
  display: flex;
  padding: 8px 0 0;
  position: absolute;
  align-items: flex-start;
  flex-shrink: 0;
  flex-direction: column;
}
.superframe-container30 {
  gap: 16px;
  width: 146px;
  display: flex;
  align-items: flex-start;
  flex-shrink: 0;
  justify-content: space-between;
}
.superframe-filled-black {
  width: 38px;
  height: 38px;
  display: flex;
  overflow: hidden;
  position: relative;
  left: 30px;
  background: linear-gradient(
    180deg,
    rgba(71, 83, 97, 1) 0%,
    rgba(29, 29, 29, 1) 100%
  );
  align-items: flex-start;
  flex-shrink: 0;
  border-radius: 250px;
}
.superframe-artboard {
  top: 11.438013076782227px;
  left: 7.181987762451172px;
  width: 20.634000778198242px;
  height: 17.09999656677246px;
  display: flex;
  position: absolute;
  align-items: flex-start;
  flex-shrink: 1;
}
.superframe-path {
  top: 0px;
  left: 0px;
  width: 21px;
  height: 17px;
  position: absolute;
}
.superframe-component41 {
  width: 38px;
  height: 38px;
  display: flex;
  position: relative;
  align-items: flex-start;
  flex-shrink: 0;
  border-radius: 19px;
  background-color: rgba(37, 38, 38, 1);
}
.superframe-image3 {
  top: 7px;
  left: 7px;
  width: 24px;
  height: 24px;
  display: flex;
  position: absolute;
  align-items: flex-start;
  flex-shrink: 0;
  flex-direction: column;
}
.superframe-sv-gsprite18svgfill1 {
  width: 24px;
  height: 24px;
}
.superframe-component42 {
  width: 38px;
  height: 38px;
  display: flex;
  position: relative;
  align-items: flex-start;
  flex-shrink: 0;
  border-radius: 19px;
  background-color: rgba(37, 38, 38, 1);
}
.superframe-image4 {
  top: 7px;
  left: 7px;
  width: 24px;
  height: 24px;
  display: flex;
  position: absolute;
  align-items: flex-start;
  flex-shrink: 0;
  flex-direction: column;
}
.superframe-sv-gsprite18svgfill2 {
  width: 24px;
  height: 24px;
}
.superframe-margin20 {
  top: 586px;
  left: 388px;
  width: 752px;
  display: flex;
  padding: 0 0 39px;
  position: absolute;
  align-items: flex-end;
  flex-shrink: 0;
  flex-direction: column;
}
.superframe-overlay2 {
  top: -363px;
  left: -4px;
  width: 752px;
  height: 91px;
  display: flex;
  padding: 0 28px 28px 22px;
  position: absolute;
  align-items: flex-start;
  flex-shrink: 0;
  border-radius: 24px;
  flex-direction: column;
  background-color: #2d3133;
}
.superframe-margin21 {
  width: 573px;
  height: 88px;
  display: flex;
  padding: 2px 0 6px;
  align-items: flex-start;
  flex-shrink: 0;
  flex-direction: column;
}
.superframe-container31 {
  gap: -2.842170943040401e-14px;
  width: 689px;
  height: 53px;
  display: flex;
  align-items: flex-start;
  flex-shrink: 0;
}
.superframe-text73 {
  color: #ffffff;
  width: 573px;
  height: auto;
  font-size: 26px;
  box-shadow: rgba(0, 0, 0, 0.25) 0px 4px 4px 0px;
  font-style: Light;
  text-align: left;
  font-family: Source Sans Pro;
  font-weight: 300;
  line-height: 32px;
  font-stretch: normal;
  text-decoration: none;
}
.superframe-text74 {
  font-weight: 300;
}
.superframe-text75 {
  font-weight: 600;
}
.superframe-text77 {
  color: rgba(10, 163, 136, 1);
  width: 93px;
  height: auto;
  text-align: right;
  line-height: 30px;
  font-size: 40px;
}
.superframe-spv {
  width: 16px;
  height: 16px;
  display: flex;
  z-index: 2;
  overflow: hidden;
  position: relative;
  align-items: flex-start;
  flex-shrink: 0;
}
</style>
