<template>
	<section class="_margin-left:5 _margin-right:5 _margin-top:2">
		<h1>About</h1>

		<h2>What is Poger?</h2>
		<hr/>
		<p>
			<b>Poger</b> is an activity started by my friend group in March of 2022, when a bunch of us recommended songs that we liked and put it into a shared playlist. 
			From there, we slowly turned it into a fun social activity that you can do as well! A typical poge consists of these steps:
		</p>
		<ol>
			<li>Each participant puts in 4-6 (typically 5) songs into a collaborative Spotify playlist.</li>
			<li>After that, someone streams the shuffled playlist to everyone.</li>
			<li>Enjoy a mix of everyone's music.</li>
		</ol>
		<p>
			That's really all there is to it! 
		</p>
		<ICollapsible class="_margin-bottom:1">
			<ICollapsibleItem title="Poger Modifications">
				<p>After a while, you might want to have a little more fun with Poger - there are plenty of variations you can try!</p>

				<h6><i>Competitive Poger:</i></h6> 
				<p>
					In this variation, instead of casually listening to music, you have to guess who put in the song you're listening to!
					This is a fun variant to play after you all have listened to a bunch of music from each other, to better get a sense of each other's music tastes.
				</p>
				<p>
					A fun strategy with competitive poger is <i>baiting</i>, where a player might intentionally put in songs they listen to that math a different player's music tastes.
				</p>

				<h6><i>Themed Poger:</i></h6>
				<p>
					Another fun variation is setting specific <i>themes</i> for the poger - such as requiring all the songs to be a specific genre, international, instrumental, or have female singers.
					These offer a lot of variety and give people chances to show off music that they might not show in a normal poger.
				</p>
			</ICollapsibleItem>
		</ICollapsible>

		<h2>What is a Stuwant?</h2>
		<hr/>
		<p>
			A <b>stuwant</b> simply refers to a member of the group of original Poger participants. 
			The name comes from when we tried to create a playlist cover image using Dall-E - it produced a penguin with the text "stuwants of poge" above it. 
			We ultimately decided to call ourselves that afterwards.
		</p>
		<IAlert color="info" class="_margin-bottom:1">
			<template #icon>
				<IIcon name="ink-info" />
			</template>
			<p>Want to see the Stuwants of Poge image? Check out <b>gamer is goger</b> in the <NuxtLink to="/pogers">Pogers</NuxtLink> page.</p>
		</IAlert>

		<h2>Why is it called Poger?</h2>
		<hr/>
		<p>That's a secret for the original participants to know. 😉</p>
	</section>
</template>