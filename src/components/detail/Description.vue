<template>
    <div>
        <div class="card">
            <div class="detail">
                <p class="card-header-title">
                    {{detail.title}}
                </p>
                <div class="content">
                    <ul>
                        <li v-for="(item, index) in detail.items" :key="index">
                            {{item.value}}
                        </li>
                    </ul>
                </div>
            </div>
            <div class="description">
                <p class="card-header-title">
                    {{description.title}}
                </p>
                <div class="context">
                    <span v-for="(item, index) in description.items" :key="index">
                        {{item.value}}
                    </span>
                </div>
            </div>
            <div class="shipping">
                <p class="card-header-title">
                    {{shipping.title}}
                </p>
                <div class="content">
                    <ul>
                        <li v-for="(item, index) in shipping.items" :key="index">
                            {{item.value}}
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Description",
        data() {
            return {
                detail: {
                    title: "DETAILS",
                    items: [
                        {key: "", value: "Model is 5′7″Wearing size S"},
                        {key: "", value: "65% Extra Fine Merino Wool, 35% Polyamide"},
                        {key: "", value: "Italian Wool"},
                        {key: "", value: "Questions about fit? Email"},
                    ]
                },
                description: {
                    title: "DESCRIPTION",
                    items: [
                        {key: "", value: "Our coziest sweater ever. Made of premium Italian yarn, the Teddy Crew Neck Sweater has the look and feel of elevated knitwear with a crazy-soft, snuggly texture. Complete with an easy cropped length, a wider neckline, and a slightly nipped waist, it’s so cozy, you might even fall asleep standing up."},
                    ]
                },
                shipping: {
                    title: "SHIPPING & RETURNS",
                    items: [
                        {key: "", value: "Shipping is an additional 1-10 business days depending on location. Shipping time will be provided at checkout."},
                        {key: "", value: "Free returns are available for standard sizes within 15 days. Custom sizes are final sale."},
                    ]
                }
            }
        }
    }
</script>

<style scoped>
    .card {
        width: 100%;
        margin-top: 20px;
        height: 200px;
    }
    .card > * {
        font-size: small;
    }
    .card > .detail, .card > .description, .card > .shipping {
        width: 30%;
        float: left;
    }
    .card > .description {
        width: 40%;
    }
</style>