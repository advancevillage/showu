<template>
    <div class="modal-card">
        <div class="address">
            <label :for="languages.Address.country[language]">

            </label>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Address",
        props: {
            language: {
                type: String,
                required: true
            }
        },
        data() {
            return {
                languages: this.$languages,
                country: "",
            }
        }
    }
</script>

<style scoped>
    .modal-card {
        width: 600px;
        height: 400px;
        flex-direction: row;
        background: rgb(192,192,192);
    }
</style>