<template>
    <div>
        <div id="drop-in-container"></div>
        <button v-if="paymentOption === 'card'" id="btn-pay" @click.prevent="Purchase">{{this.languages.Order.credit[this.language]}}</button>
    </div>
</template>

<script>
    import BrainTree from 'braintree-web-drop-in'
    
    export default {
        name: "Pay",
        data() {
            return {
                languages: this.$languages,
                language: "chinese",
                instance: {},
                authorization: "eyJ2ZXJzaW9uIjoyLCJlbnZpcm9ubWVudCI6InNhbmRib3giLCJhdXRob3JpemF0aW9uRmluZ2VycHJpbnQiOiJleUowZVhBaU9pSktWMVFpTENKaGJHY2lPaUpGVXpJMU5pSXNJbXRwWkNJNklqSXdNVGd3TkRJMk1UWXRjMkZ1WkdKdmVDSXNJbWx6Y3lJNklrRjFkR2g1SW4wLmV5SmxlSEFpT2pFMU9EUTROVFkxTWpjc0ltcDBhU0k2SW1FME9UTXdOamxpTFRJNU4yTXROR0poWmkxaU5tTXpMVGxsT0dJNFltTXdZV00xTlNJc0luTjFZaUk2SWpNMFpqaHJNbVJ0Y25remFHTnpPVzBpTENKcGMzTWlPaUpCZFhSb2VTSXNJbTFsY21Ob1lXNTBJanA3SW5CMVlteHBZMTlwWkNJNklqTTBaamhyTW1SdGNua3phR056T1cwaUxDSjJaWEpwWm5sZlkyRnlaRjlpZVY5a1pXWmhkV3gwSWpwMGNuVmxmU3dpY21sbmFIUnpJanBiSW0xaGJtRm5aVjkyWVhWc2RDSmRMQ0p2Y0hScGIyNXpJanA3SW0xbGNtTm9ZVzUwWDJGalkyOTFiblJmYVdRaU9pSXpOR1k0YXpKa2JYSjVNMmhqY3psdEluMTkuNVZJalRNZXdCdGl5R21GMlcxbzhiY0Q0OTdJNTFFTC1qQ0U0eXVjSXdFbXZ3elY1TzlUVE5xVi1tNkhqTnVicHEwQUlJaElXRGxVeDM4SEJSelFKT1EiLCJjb25maWdVcmwiOiJodHRwczovL2FwaS5zYW5kYm94LmJyYWludHJlZWdhdGV3YXkuY29tOjQ0My9tZXJjaGFudHMvMzRmOGsyZG1yeTNoY3M5bS9jbGllbnRfYXBpL3YxL2NvbmZpZ3VyYXRpb24iLCJncmFwaFFMIjp7InVybCI6Imh0dHBzOi8vcGF5bWVudHMuc2FuZGJveC5icmFpbnRyZWUtYXBpLmNvbS9ncmFwaHFsIiwiZGF0ZSI6IjIwMTgtMDUtMDgifSwiY2hhbGxlbmdlcyI6WyJjdnYiXSwiY2xpZW50QXBpVXJsIjoiaHR0cHM6Ly9hcGkuc2FuZGJveC5icmFpbnRyZWVnYXRld2F5LmNvbTo0NDMvbWVyY2hhbnRzLzM0ZjhrMmRtcnkzaGNzOW0vY2xpZW50X2FwaSIsImFzc2V0c1VybCI6Imh0dHBzOi8vYXNzZXRzLmJyYWludHJlZWdhdGV3YXkuY29tIiwiYXV0aFVybCI6Imh0dHBzOi8vYXV0aC52ZW5tby5zYW5kYm94LmJyYWludHJlZWdhdGV3YXkuY29tIiwiYW5hbHl0aWNzIjp7InVybCI6Imh0dHBzOi8vb3JpZ2luLWFuYWx5dGljcy1zYW5kLnNhbmRib3guYnJhaW50cmVlLWFwaS5jb20vMzRmOGsyZG1yeTNoY3M5bSJ9LCJ0aHJlZURTZWN1cmVFbmFibGVkIjp0cnVlLCJwYXlwYWxFbmFibGVkIjp0cnVlLCJwYXlwYWwiOnsiZGlzcGxheU5hbWUiOiJzaG93dSIsImNsaWVudElkIjoiQWRNWnZfUjdzZ1BZTlc1YVNOdmNKNnBGQnVTQmk2TnNsYzI4WmdrMzQzcTNObmppU1RMTHQzaFkyN1NPVHNxU0hqQW9yQUhlSnhPMG1GOGciLCJwcml2YWN5VXJsIjoiaHR0cDovL2V4YW1wbGUuY29tL3BwIiwidXNlckFncmVlbWVudFVybCI6Imh0dHA6Ly9leGFtcGxlLmNvbS90b3MiLCJiYXNlVXJsIjoiaHR0cHM6Ly9hc3NldHMuYnJhaW50cmVlZ2F0ZXdheS5jb20iLCJhc3NldHNVcmwiOiJodHRwczovL2NoZWNrb3V0LnBheXBhbC5jb20iLCJkaXJlY3RCYXNlVXJsIjpudWxsLCJhbGxvd0h0dHAiOnRydWUsImVudmlyb25tZW50Tm9OZXR3b3JrIjpmYWxzZSwiZW52aXJvbm1lbnQiOiJvZmZsaW5lIiwidW52ZXR0ZWRNZXJjaGFudCI6ZmFsc2UsImJyYWludHJlZUNsaWVudElkIjoibWFzdGVyY2xpZW50MyIsImJpbGxpbmdBZ3JlZW1lbnRzRW5hYmxlZCI6dHJ1ZSwibWVyY2hhbnRBY2NvdW50SWQiOiJzaG93dSIsImN1cnJlbmN5SXNvQ29kZSI6IlVTRCJ9LCJtZXJjaGFudElkIjoiMzRmOGsyZG1yeTNoY3M5bSIsInZlbm1vIjoib2ZmIiwibWVyY2hhbnRBY2NvdW50SWQiOiIzNGY4azJkbXJ5M2hjczltIn0=",
                locale: "zh_CN",
                paypal: {
                    flow: "vault"
                },
                paymentOption: "",
                payInfo: {}
            }
        },
        mounted() {
            this.CreatePayToken();
            BrainTree.create({authorization: this.authorization, selector: "#drop-in-container", paypal: this.paypal})
                .then(instance => {
                    let _this = this;
                    instance.on('paymentOptionSelected', function(option) {
                        _this.paymentOption = option.paymentOption;
                    });
                    this.instance = instance;
                })
                .catch(err => {
                    console.error(err);
                })
        },
        methods: {
            Purchase() {
                let _this = this;
                _this.instance.requestPaymentMethod({}, function (err, payload) {
                    if (err) {
                        console.error(err);
                    } else {
                        _this.payInfo = payload;
                        _this.$emit("selectPay", _this.payInfo)
                    }
                });
            },
            async CreatePayToken() {
                const headers = {
                    "x-language": this.language,
                };
                const body = {};
                this.authorization = await this.$api.CreatePayToken(headers, body);
            }
        }
    }
</script>

<style scoped>
    #btn-pay {
        background: #000000;
        border-radius: 0.25rem;
        border: 0;
        cursor: pointer;
        color: white;
        display: inline-block;
        font-weight: 500;
        text-decoration: none;
        transition: all 150ms cubic-bezier(0.77,0,0.175,1);
        font-size: 0.875rem;
        width: 100%;
        height: 2rem;
        letter-spacing: 1rem;
        outline: none;
    }
    #btn-pay:hover {
        background: #1524d9;
        transition: all 150ms cubic-bezier(0.77,0,0.175,1);
        color:white;
    }
</style>