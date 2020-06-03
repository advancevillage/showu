<template>
    <div class="ss_checkout">
        <div class="ss_header">
            <!-- 头部栏 -->
            <Header :width="width" :height="height * 0.13" :opacity=false />
        </div>
        <div class="ss_content">
            <div class="ss_detail">
                <Back :width="width * 0.6" :height="height * 0.05" go="/" :title="languages.OPERATE.BACK[language]"/>
                <Step :items="steps" :width="width * 0.6" :height="height * 0.13" :id="step"/>
            </div>
            <div class="ss_summary"></div>
        </div>
    </div>
</template>

<script>
    import Header from "../components/Business/Header";
    import Back   from "../components/Basic/Back"
    import Step   from "../components/Basic/Step"


    export default {
        name: "Checkout",
        components: {
            Back,
            Header,
            Step,
        },
        data() {
            return {
                languages: this.$languages,
                language: "zh_CN",
                width: window.screen.availWidth,
                height: window.screen.availHeight,
                steps: [],
                step: 1
            }
        },
        mounted() {
            this.steps.push({icon: "mdi mdi-account", label: this.languages.NOUN.ACCOUNT[this.language]})
            this.steps.push({icon: "mdi mdi-home", label: this.languages.NOUN.ADDRESS[this.language]});
            this.steps.push({icon: "mdi mdi-credit-card", label: this.languages.NOUN.PAY[this.language]});
        }
    }
</script>

<style scoped>
    .ss_header, .ss_content{
        float: left;
        width: 100%;
    }
    .ss_detail, .ss_summary {
        float: left;
        width: 100%;
        height: 100%;
        padding: 0 5%;
        border: 1px solid red;
    }
</style>