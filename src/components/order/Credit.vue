<template>
    <div class="credit_card">
        <ul>
            <li class="credit_logo">
                <img :src="url" alt="logos"/>
            </li>
            <li class="credit_number">
                <label>
                    <input v-model="card.number" type="text" name="credit_number" minlength="16" maxlength="16" readonly="readonly" disabled="disabled"/>
                </label>
            </li>
            <li class="credit_expire">
                 <div style="float: right;margin: 0 5%;text-align: center;">
                     <div style="font-size: 0.1rem;color: darkgray;">Month/Year</div>
                     <div style="font-size: 1rem;">{{this.card.month}}/{{this.card.year}}</div>
                 </div>
            </li>
            <li class="credit_your_name">
                <span>{{this.card.yourName}}</span>
            </li>
        </ul>
    </div>
</template>

<script>
    export default {
        name: "Credit",
        props: {
            card: {
                type: Object,
                required: true
            }
        },
        data() {
            return {
                image: "https://www.merchantequip.com/image",
                height: 32,
                url: "",
            }
        },
        mounted() {
            this.CreateCreditLogo()
        },
        methods: {
            CreateCreditLogo() {
                let bg = "bgcolor=808080";
                let h  = "height=" + this.height;
                let l  = "logos="  + this.card.logo;
                this.url = this.image + "?" + bg + "&" + h + "&" + l
            }
        }
    }
</script>

<style scoped>
    .credit_card {
        height: 150px;
        width: 237px;
        border-radius: 8%;
        background: rgb(128, 128, 128);
        color: white;
    }
    .credit_logo, .credit_number, .credit_expire, .credit_your_name {
        height: 40px;
        width: 100%;
        font-family: serif;
    }
    .credit_your_name {
        height: 30px;
        padding: 0 20px;
        font-size: 1rem;
        text-transform: capitalize;
        position: relative;
        top: -20px;
    }
    .credit_logo > img {
        margin: 4px;
    }
    .credit_number input {
        width: 100%;
        height: 100%;
        border: none;
        font-size: medium;
        letter-spacing: 5px;
        text-align: center;
        background: rgb(128, 128, 128);
        color: white;
    }
    .credit_expire {
        padding: 5px 0;
        text-transform: capitalize;
    }
</style>