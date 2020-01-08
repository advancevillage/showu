<template>
    <div>
        <div class="detail_size">
            <section>
                <b-tag class="size" v-for="(item, index) in context" :key="index">{{item}}</b-tag>
            </section>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Size",
        data() {
            return {
                context: ["XS/36", "S/37", "L/42", "M/43", "L"]
            }
        }
    }
</script>

<style scoped>
    .size {
        width: 40px;
        height: 20px;
        margin: 0 2px;
    }
    .size:hover {
        background: darkgray;
    }
</style>