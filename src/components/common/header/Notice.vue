<template>
    <div>
        <!-- 通知栏 -->
        <nav class="level">
            <p class="level-item has-text-centered"></p>
            <p class="level-item has-text-centered"><a class="notice_text">{{noticeText}}</a></p>
            <p class="level-item has-text-centered"></p>
            <!-- Right side -->
            <div class="level-right">
                <select
                    v-model="lang"
                    class="country"
                    v-on:change="ChangeLanguage">
                    <option v-for="(item, index) in country" :key="index" v-bind:value="item.lang.toLowerCase()">{{item.key.toUpperCase()}}</option>
                </select>
            </div>
        </nav>
    </div>
</template>

<script>
    export default {
        name: "Notice",
        props: {
            language: {
                type: String,
                required: true,
            },
        },
        data() {
            return {
                lang: this.language,
                noticeText: "Show You! More Confident And Beautiful",
                country: [
                    {key: "cn", lang: "chinese"},
                    {key: "en", lang: "english"}
                ],
            }
        },
        methods: {
            ChangeLanguage() {
                this.$emit("selectedLanguage", this.lang);
            }
        }
    }
</script>

<style scoped>
    .notice_text {
        color: white;
        text-align: center;
        text-decoration: underline;
    }
    .country {
        border: none;
        background: black;
        color: white;
        height: 22px;
    }
    .level-right select:focus {
        outline: none;
    }
</style>