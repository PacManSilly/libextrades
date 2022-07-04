<script setup>
/* eslint-disable */
import { ref, computed, onMounted } from 'vue'

// props
const props = defineProps({
    coin: {type: Object}
})

// data
const change = ref("")
const price = ref("000.00")

// computed
const changeIsNegative = computed(() => {
    // check if the coin price change percent is negative by searching
    // for a negative "-" sign in its percent data.
    return change.value.includes('-');
})

// methods
const websocketRequest = (pair) => {
    // method to make websocket request to a ws server
    const binance = `wss://stream.binance.com:9443/ws/${pair}@ticker`;
    const ws = new WebSocket(binance)

    ws.onmessage = (resp) => {
        const jsonResp = JSON.parse(resp.data)
        // console.log(jsonResp)

        // update the coinData price and change in percentage.
        price.value = jsonResp.c
        change.value = jsonResp.P
    }
}

const formatNumber = (value, decimal = 2) => {
        // method to format numeric values into financial display.
        var seperatedValues = []
        var seperatedString = ""
        var afterDecimal =  ""

        value = String(value)

        // does value have a decimal point?
        if (value.includes('.')) {
            // split by '.', then get value after the decimal 'first'.
            afterDecimal = '.' + value.split('.')[1].slice(0, decimal)
            // and then value should now = value before the decimal
            value = value.split('.')[0]
        }
        // if value has no decimal, leave as is
        else value

        // is the value over a thousand?, is it greater than 3 in length?
        if (value.length > 3) {
            // then turn value into array for better indexing
            value = value.split('')

            while (value.length > 3) {
                // splice values in three's, from the 3rd last to the last value and
                // insert the values into the seperatedValues array using the unshift
                // method to retain the array index positions.
                seperatedValues.unshift(value.splice(-3, ))
            }

            // loop over the values in the seperatedValues array and concatenate to each order
            // removing the ',' commas inserted and assign it to seperatedString
            for (const value in seperatedValues) {
                seperatedString += seperatedValues[value].toString().replaceAll(',','') + ','
            }

            // set the formatted value
            value = value.toString().replaceAll(',', '')
                    + ','
                    + seperatedString.slice(0, seperatedString.lastIndexOf(','))
                    + afterDecimal

            // return the new value
            return value
        }
        // if the value is less than a thousand, less than 3 in length?
        // and has a decimal point.
        else {
            return value = value + afterDecimal
            
        }
    }

onMounted(() => {
    websocketRequest(props.coin.pair);
})
</script>

<template>
	<div>
		<div class="flex flex-col">
			<!-- svg, name and change -->
			<div class="flex gap-2 items-center">
				<img :src="coin.icon" class="w-9 h-9" />
				<p class="text-slate-200 text-base font-bold">{{coin.name}}</p>
				<p :class="changeIsNegative ? 'text-red-600':'text-green-600'" class="text-xs">{{formatNumber(change)}}</p>
			</div>

			<!-- pair and price -->
			<div class="flex flex-col ml-11 text-slate-500">
				<p class=" text-xs font-bold uppercase">{{coin.pair}}</p>
				<p class="text-xs font-bold">${{formatNumber(price)}}</p>
			</div>
		</div>
	</div>
</template>
