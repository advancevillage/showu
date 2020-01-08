<template>
    <div>
        <div class="detail_style">
            <section>
                <b-tag class="style" v-for="(item, index) in context" :key="index">{{item}}</b-tag>
            </section>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Style",
        data() {
            return {
                context: ["Tanks", "Tees", "Dress", "Boho"]
            }
        }
    }
</script>

<style scoped>
    .style {
        width: 40px;
        height: 20px;
        margin: 0 2px;
    }
    .style:hover {
        background: darkgray;
    }
</style>